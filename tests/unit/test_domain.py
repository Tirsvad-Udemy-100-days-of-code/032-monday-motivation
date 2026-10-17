import random
from datetime import date, timedelta

import pytest

from monday_motivation.domain.errors import NoQuotesError
from monday_motivation.domain.quotes import pick_random_quote
from monday_motivation.domain.weekday import is_monday

MONDAY_DATE = date(2026, 10, 19)


def test_is_monday_true_for_monday() -> None:
    assert is_monday(MONDAY_DATE) is True


@pytest.mark.parametrize("offset", range(1, 7))
def test_is_monday_false_for_other_weekdays(offset: int) -> None:
    assert is_monday(MONDAY_DATE + timedelta(days=offset)) is False


def test_pick_random_quote_repeats_with_same_seed() -> None:
    quotes = [f"quote {number}" for number in range(20)]
    first = pick_random_quote(quotes, random.Random(7))
    second = pick_random_quote(quotes, random.Random(7))
    assert first == second


def test_pick_random_quote_returns_member_of_list() -> None:
    quotes = ["a", "b", "c"]
    assert pick_random_quote(quotes, random.Random(1)) in quotes


def test_pick_random_quote_returns_only_item() -> None:
    assert pick_random_quote(["only"], random.Random(1)) == "only"


def test_pick_random_quote_raises_for_empty_list() -> None:
    with pytest.raises(NoQuotesError):
        pick_random_quote([], random.Random(1))
