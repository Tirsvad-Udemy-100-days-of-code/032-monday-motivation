"""@brief The settings needed to log in and send.

@file mail_settings.py
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MailSettings:
    """@brief Sender, app password and recipient of the Monday email.

    The app password is left out of the representation so that it cannot reach
    a log or a traceback by accident.
    """

    sender: str
    token: str = field(repr=False)
    recipient: str
