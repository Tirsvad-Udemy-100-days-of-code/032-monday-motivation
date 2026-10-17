import smtplib
from email.message import EmailMessage
from types import TracebackType


class FakeSmtp:
    """A recording stand-in for smtplib.SMTP; it never opens a connection."""

    def __init__(self) -> None:
        self.opened: list[tuple[str, int]] = []
        self.calls: list[str] = []
        self.login_arguments: tuple[str, str] | None = None
        self.sent: list[EmailMessage] = []

    def __call__(self, host: str, port: int) -> "FakeSmtp":
        self.opened.append((host, port))
        return self

    def __enter__(self) -> "FakeSmtp":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        return None

    def starttls(self) -> None:
        self.calls.append("starttls")

    def login(self, user: str, password: str) -> None:
        self.calls.append("login")
        self.login_arguments = (user, password)

    def send_message(self, msg: EmailMessage) -> None:
        self.calls.append("send_message")
        self.sent.append(msg)


class AuthFailingSmtp(FakeSmtp):
    """Refuses the login, as a server does for a wrong app password."""

    def login(self, user: str, password: str) -> None:
        raise smtplib.SMTPAuthenticationError(535, b"bad credentials")


class UnreachableSmtp(FakeSmtp):
    """Cannot reach the server."""

    def __call__(self, host: str, port: int) -> "FakeSmtp":
        raise OSError("network down")
