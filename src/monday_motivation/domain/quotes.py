"""@brief The random choice of a quote.

@file quotes.py
"""

import random
from collections.abc import Sequence

from monday_motivation.domain.errors import NoQuotesError


def pick_random_quote(quotes: Sequence[str], rng: random.Random) -> str:
    """@brief Choose one quote by chance.

    @param quotes The quotes to choose from.
    @param rng The random generator; a test hands in a seeded one.
    @return One entry of the list.
    @raises NoQuotesError When the list is empty.
    """
    if not quotes:
        raise NoQuotesError("There is no quote to choose from.")
    return rng.choice(quotes)
