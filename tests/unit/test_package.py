import monday_motivation
from monday_motivation import constants


def test_package_has_a_version() -> None:
    assert monday_motivation.__version__


def test_constants_name_monday_as_weekday_zero() -> None:
    assert constants.MONDAY == 0


def test_constants_name_the_mail_subject() -> None:
    assert constants.MAIL_SUBJECT == "Monday Motivation"
