import pytest

from monday_motivation.application.mail_settings import MailSettings
from monday_motivation.constants import SMTP_HOST, SMTP_PORT
from monday_motivation.domain.errors import MailSendError
from monday_motivation.infrastructure.smtp_mailer import build_message, send_email
from tests.fakes import AuthFailingSmtp, FakeSmtp, UnreachableSmtp

TOKEN = "fake-token-value"
SETTINGS = MailSettings(
    sender="from@example.test", token=TOKEN, recipient="to@example.test"
)


def test_build_message_sets_subject() -> None:
    message = build_message("a@example.test", "b@example.test", "Go on")
    assert message["Subject"] == "Monday Motivation"


def test_build_message_sets_sender_and_recipient() -> None:
    message = build_message("a@example.test", "b@example.test", "Go on")
    assert (message["From"], message["To"]) == ("a@example.test", "b@example.test")


def test_build_message_body_contains_quote() -> None:
    message = build_message("a@example.test", "b@example.test", "Go on")
    assert "Go on" in message.get_content()


def test_send_email_calls_starttls_login_send_in_order() -> None:
    fake = FakeSmtp()
    send_email(build_message("a@example.test", "b@example.test", "x"), SETTINGS, fake)
    assert fake.calls == ["starttls", "login", "send_message"]


def test_send_email_logs_in_with_sender_and_token() -> None:
    fake = FakeSmtp()
    send_email(build_message("a@example.test", "b@example.test", "x"), SETTINGS, fake)
    assert fake.login_arguments == (SETTINGS.sender, TOKEN)


def test_send_email_opens_gmail_host_and_port() -> None:
    fake = FakeSmtp()
    send_email(build_message("a@example.test", "b@example.test", "x"), SETTINGS, fake)
    assert fake.opened == [(SMTP_HOST, SMTP_PORT)]


def test_send_email_hands_over_the_message() -> None:
    fake = FakeSmtp()
    message = build_message("a@example.test", "b@example.test", "x")
    send_email(message, SETTINGS, fake)
    assert fake.sent == [message]


def test_send_email_wraps_authentication_error() -> None:
    message = build_message("a@example.test", "b@example.test", "x")
    with pytest.raises(MailSendError) as info:
        send_email(message, SETTINGS, AuthFailingSmtp())
    assert info.value.__cause__ is not None
    assert TOKEN not in str(info.value)


def test_send_email_wraps_os_error() -> None:
    message = build_message("a@example.test", "b@example.test", "x")
    with pytest.raises(MailSendError) as info:
        send_email(message, SETTINGS, UnreachableSmtp())
    assert isinstance(info.value.__cause__, OSError)
    assert TOKEN not in str(info.value)
