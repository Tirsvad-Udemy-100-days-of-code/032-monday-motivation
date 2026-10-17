import pytest

from monday_motivation.application.mail_settings import MailSettings
from monday_motivation.constants import ENV_RECIPIENT, ENV_SENDER, ENV_TOKEN
from monday_motivation.domain.errors import MissingSettingError
from monday_motivation.infrastructure.env_settings import load_settings

SENDER = "from@example.test"
TOKEN = "fake-token-value"
RECIPIENT = "to@example.test"


def _environ() -> dict[str, str]:
    return {ENV_SENDER: SENDER, ENV_TOKEN: TOKEN, ENV_RECIPIENT: RECIPIENT}


def test_load_settings_reads_all_three_values() -> None:
    settings = load_settings(_environ())
    assert (settings.sender, settings.token, settings.recipient) == (
        SENDER,
        TOKEN,
        RECIPIENT,
    )


@pytest.mark.parametrize("name", [ENV_SENDER, ENV_TOKEN, ENV_RECIPIENT])
def test_load_settings_names_missing_variable(name: str) -> None:
    environ = _environ()
    del environ[name]
    with pytest.raises(MissingSettingError) as info:
        load_settings(environ)
    assert name in str(info.value)


@pytest.mark.parametrize("name", [ENV_SENDER, ENV_TOKEN, ENV_RECIPIENT])
def test_load_settings_rejects_blank_variable(name: str) -> None:
    environ = _environ()
    environ[name] = "   "
    with pytest.raises(MissingSettingError):
        load_settings(environ)


def test_load_settings_error_does_not_contain_any_value() -> None:
    environ = _environ()
    del environ[ENV_RECIPIENT]
    with pytest.raises(MissingSettingError) as info:
        load_settings(environ)
    message = str(info.value)
    assert SENDER not in message
    assert TOKEN not in message


def test_mail_settings_repr_hides_token() -> None:
    settings = MailSettings(sender=SENDER, token=TOKEN, recipient=RECIPIENT)
    assert TOKEN not in repr(settings)
