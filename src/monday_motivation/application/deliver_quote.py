"""@brief The use case: deliver one quote on a Monday.

@file deliver_quote.py
"""

import random
from collections.abc import Callable, Sequence
from datetime import date

from monday_motivation.domain.quotes import pick_random_quote
from monday_motivation.domain.weekday import is_monday


def deliver_monday_quote(
    today: date,
    quotes: Sequence[str],
    rng: random.Random,
    deliver: Callable[[str], None],
    *,
    force: bool = False,
) -> bool:
    """@brief Choose a quote and hand it to the delivery function on a Monday.

    @param today The date of the run.
    @param quotes The quotes to choose from.
    @param rng The random generator.
    @param deliver Called with the chosen quote; it sends or shows it.
    @param force Skip the Monday check (for testing on any day).
    @return True when a quote was delivered, False when it was not a Monday.
    """
    if not force and not is_monday(today):
        return False
    deliver(pick_random_quote(quotes, rng))
    return True
