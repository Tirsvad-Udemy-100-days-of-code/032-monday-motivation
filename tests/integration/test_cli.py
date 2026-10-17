import io
import random
import sys
from datetime import date
from pathlib import Path

import pytest

from monday_motivation.constants import ENV_RECIPIENT, ENV_SENDER, ENV_TOKEN
from monday_motivation.presentation import cli
from monday_motivation.presentation.cli import main
from tests.fakes import FakeSmtp

MONDAY_DATE = date(2026, 10, 19)
TUESDAY_DATE = date(2026, 10, 20)
TOKEN = "fake-token-value"
ENVIRON = {
    ENV_SENDER: "from@example.test",
    ENV_TOKEN: TOKEN,
    ENV_RECIPIENT: "to@example.test",
}


def _quotes_file(tmp_path: Path) -> Path:
    path = tmp_path / "quotes.txt"
    path.write_text("Keep going\n", encoding="utf-8")
    return path


def test_main_dry_run_prints_subject_and_quote_without_sending(
    tmp_path: Path,
) -> None:
    fake, out, err = FakeSmtp(), io.StringIO(), io.StringIO()
    code = main(
        ["--dry-run", "--force", "--quotes", str(_quotes_file(tmp_path))],
        today=TUESDAY_DATE,
        environ={},
        smtp_factory=fake,
        rng=random.Random(1),
        out=out,
        err=err,
    )
    assert code == 0
    assert "Dry run: nothing is sent." in out.getvalue()
    assert "Subject: Monday Motivation" in out.getvalue()
    assert "Keep going" in out.getvalue()
    assert fake.opened == []


def test_main_prints_not_monday_line_on_tuesday(tmp_path: Path) -> None:
    fake, out = FakeSmtp(), io.StringIO()
    code = main(
        ["--quotes", str(_quotes_file(tmp_path))],
        today=TUESDAY_DATE,
        environ=ENVIRON,
        smtp_factory=fake,
        out=out,
        err=io.StringIO(),
    )
    assert code == 0
    assert "Today is not a Monday: nothing was sent." in out.getvalue()
    assert fake.opened == []


def test_main_sends_through_factory_on_monday(tmp_path: Path) -> None:
    fake, out = FakeSmtp(), io.StringIO()
    code = main(
        ["--quotes", str(_quotes_file(tmp_path))],
        today=MONDAY_DATE,
        environ=ENVIRON,
        smtp_factory=fake,
        rng=random.Random(1),
        out=out,
        err=io.StringIO(),
    )
    assert code == 0
    assert fake.calls == ["starttls", "login", "send_message"]
    assert "Sent a Monday email to to@example.test." in out.getvalue()


def test_main_output_never_contains_token(tmp_path: Path) -> None:
    out, err = io.StringIO(), io.StringIO()
    main(
        ["--quotes", str(_quotes_file(tmp_path))],
        today=MONDAY_DATE,
        environ=ENVIRON,
        smtp_factory=FakeSmtp(),
        out=out,
        err=err,
    )
    assert TOKEN not in out.getvalue() + err.getvalue()


def test_main_missing_setting_exits_one_and_names_variable(tmp_path: Path) -> None:
    environ = {ENV_SENDER: "from@example.test", ENV_RECIPIENT: "to@example.test"}
    out, err = io.StringIO(), io.StringIO()
    code = main(
        ["--quotes", str(_quotes_file(tmp_path))],
        today=MONDAY_DATE,
        environ=environ,
        smtp_factory=FakeSmtp(),
        out=out,
        err=err,
    )
    assert code == 1
    assert ENV_TOKEN in err.getvalue()


def test_main_missing_quotes_file_exits_one(tmp_path: Path) -> None:
    err = io.StringIO()
    code = main(
        ["--quotes", str(tmp_path / "missing.txt")],
        today=MONDAY_DATE,
        environ=ENVIRON,
        smtp_factory=FakeSmtp(),
        out=io.StringIO(),
        err=err,
    )
    assert code == 1
    assert err.getvalue().startswith("Error: ")


def test_run_switches_standard_streams_to_utf8(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    streams = [io.TextIOWrapper(io.BytesIO(), encoding="ascii") for _ in range(2)]
    monkeypatch.setattr(sys, "stdout", streams[0])
    monkeypatch.setattr(sys, "stderr", streams[1])
    monkeypatch.setattr(cli, "main", lambda: 0)
    with pytest.raises(SystemExit):
        cli.run()
    assert [stream.encoding for stream in streams] == ["utf-8", "utf-8"]
