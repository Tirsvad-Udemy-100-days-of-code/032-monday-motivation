"""@brief Reading the mail settings from environment variables.

@file env_settings.py
"""

from collections.abc import Mapping

from monday_motivation.application.mail_settings import MailSettings
from monday_motivation.constants import ENV_RECIPIENT, ENV_SENDER, ENV_TOKEN
from monday_motivation.domain.errors import MissingSettingError


def _require(environ: Mapping[str, str], name: str) -> str:
    value = environ.get(name, "").strip()
    if not value:
        raise MissingSettingError(f"Environment variable {name} is not set.")
    return value


def load_settings(environ: Mapping[str, str]) -> MailSettings:
    """@brief Build the mail settings from the environment.

    Error messages name the variable, never its value.

    @param environ The environment, for example os.environ.
    @return The settings.
    @raises MissingSettingError When a variable is missing or empty.
    """
    return MailSettings(
        sender=_require(environ, ENV_SENDER),
        token=_require(environ, ENV_TOKEN),
        recipient=_require(environ, ENV_RECIPIENT),
    )
