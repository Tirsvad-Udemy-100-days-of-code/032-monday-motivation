import random
from datetime import date

from monday_motivation.application.deliver_quote import deliver_monday_quote

MONDAY_DATE = date(2026, 10, 19)
TUESDAY_DATE = date(2026, 10, 20)


def test_deliver_monday_quote_delivers_once_on_monday() -> None:
    delivered: list[str] = []
    result = deliver_monday_quote(
        MONDAY_DATE, ["a", "b"], random.Random(1), delivered.append
    )
    assert result is True
    assert len(delivered) == 1


def test_deliver_monday_quote_skips_on_tuesday() -> None:
    delivered: list[str] = []
    result = deliver_monday_quote(
        TUESDAY_DATE, ["a", "b"], random.Random(1), delivered.append
    )
    assert result is False
    assert delivered == []


def test_deliver_monday_quote_delivers_on_tuesday_when_forced() -> None:
    delivered: list[str] = []
    result = deliver_monday_quote(
        TUESDAY_DATE, ["a"], random.Random(1), delivered.append, force=True
    )
    assert result is True
    assert delivered == ["a"]
