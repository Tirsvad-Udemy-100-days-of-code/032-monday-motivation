"""@brief Composing and sending the Monday email over SMTP.

@file smtp_mailer.py
"""

import smtplib
from collections.abc import Callable
from contextlib import AbstractContextManager
from email.message import EmailMessage
from typing import Protocol

from monday_motivation.application.mail_settings import MailSettings
from monday_motivation.constants import MAIL_SUBJECT, SMTP_HOST, SMTP_PORT
from monday_motivation.domain.errors import MailSendError


class SmtpConnection(Protocol):
    """@brief The part of an SMTP connection that the program uses."""

    def starttls(self) -> object:
        """@brief Switch the connection to TLS."""

    def login(self, user: str, password: str) -> object:
        """@brief Log in to the mail server."""

    def send_message(self, msg: EmailMessage) -> object:
        """@brief Send a message."""


SmtpFactory = Callable[[str, int], AbstractContextManager[SmtpConnection]]


def build_message(sender: str, recipient: str, quote: str) -> EmailMessage:
    """@brief Compose the Monday email.

    @param sender The From address.
    @param recipient The To address.
    @param quote The quote for the body.
    @return The message with the subject "Monday Motivation".
    """
    message = EmailMessage()
    message["Subject"] = MAIL_SUBJECT
    message["From"] = sender
    message["To"] = recipient
    message.set_content(f"{quote}\n")
    return message


def send_email(
    message: EmailMessage,
    settings: MailSettings,
    smtp_factory: SmtpFactory = smtplib.SMTP,
) -> None:
    """@brief Log in over TLS and send the message.

    @param message The message to send.
    @param settings The sender, app password and recipient.
    @param smtp_factory Opens the connection; a test hands in a fake.
    @raises MailSendError When the server refuses or cannot be reached.
    """
    try:
        with smtp_factory(SMTP_HOST, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(settings.sender, settings.token)
            connection.send_message(message)
    except (smtplib.SMTPException, OSError) as error:
        raise MailSendError(
            f"The email could not be sent ({type(error).__name__})."
        ) from error
