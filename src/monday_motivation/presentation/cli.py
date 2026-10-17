"""@brief The command line of Monday Motivation.

@file cli.py
"""

import argparse
import io
import os
import random
import smtplib
import sys
from collections.abc import Mapping, Sequence
from datetime import date
from pathlib import Path
from typing import TextIO

from monday_motivation.application.deliver_quote import deliver_monday_quote
from monday_motivation.constants import (
    ENV_RECIPIENT,
    ENV_SENDER,
    PLACEHOLDER_RECIPIENT,
    PLACEHOLDER_SENDER,
)
from monday_motivation.domain.errors import MondayMotivationError
from monday_motivation.infrastructure.env_settings import load_settings
from monday_motivation.infrastructure.quote_file import (
    DEFAULT_QUOTES_PATH,
    read_quotes,
)
from monday_motivation.infrastructure.smtp_mailer import (
    SmtpFactory,
    build_message,
    send_email,
)


def _parse_arguments(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="monday-motivation",
        description="Send a motivational quote by email on a Monday.",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="show the email, send nothing"
    )
    parser.add_argument(
        "--force", action="store_true", help="run on any day, not only on a Monday"
    )
    parser.add_argument(
        "--quotes",
        type=Path,
        default=DEFAULT_QUOTES_PATH,
        help="quotes file, one quote per line",
    )
    return parser.parse_args(argv)


def main(
    argv: Sequence[str] | None = None,
    *,
    today: date | None = None,
    environ: Mapping[str, str] | None = None,
    smtp_factory: SmtpFactory = smtplib.SMTP,
    rng: random.Random | None = None,
    out: TextIO | None = None,
    err: TextIO | None = None,
) -> int:
    """@brief Run the program.

    @param argv The arguments; sys.argv[1:] by default.
    @param today The date of the run; today by default.
    @param environ The environment; os.environ by default.
    @param smtp_factory Opens the SMTP connection; a test hands in a fake.
    @param rng The random generator; a fresh one by default.
    @param out Where messages go; sys.stdout by default.
    @param err Where errors go; sys.stderr by default.
    @return The exit code: 0 on success or when it is not a Monday, 1 on an error.
    """
    arguments = _parse_arguments(sys.argv[1:] if argv is None else argv)
    today = date.today() if today is None else today
    environ = os.environ if environ is None else environ
    rng = random.Random() if rng is None else rng
    out = sys.stdout if out is None else out
    err = sys.stderr if err is None else err

    try:
        quotes = read_quotes(arguments.quotes)

        def deliver(quote: str) -> None:
            if arguments.dry_run:
                message = build_message(
                    environ.get(ENV_SENDER, PLACEHOLDER_SENDER),
                    environ.get(ENV_RECIPIENT, PLACEHOLDER_RECIPIENT),
                    quote,
                )
                print(
                    "Dry run: nothing is sent.\n"
                    f"From: {message['From']}\n"
                    f"To: {message['To']}\n"
                    f"Subject: {message['Subject']}\n\n"
                    f"{message.get_content()}",
                    file=out,
                )
                return
            settings = load_settings(environ)
            send_email(
                build_message(settings.sender, settings.recipient, quote),
                settings,
                smtp_factory,
            )
            print(f"Sent a Monday email to {settings.recipient}.", file=out)

        delivered = deliver_monday_quote(
            today, quotes, rng, deliver, force=arguments.force
        )
    except MondayMotivationError as error:
        print(f"Error: {error}", file=err)
        return 1
    if not delivered:
        print("Today is not a Monday: nothing was sent.", file=out)
    return 0


def run() -> None:
    """@brief Entry point of the console script and of python -m."""
    _use_utf8(sys.stdout)
    _use_utf8(sys.stderr)
    raise SystemExit(main())


def _use_utf8(stream: TextIO) -> None:
    if isinstance(stream, io.TextIOWrapper):
        stream.reconfigure(encoding="utf-8")
