"""@brief The weekday rule of the Monday email.

@file weekday.py
"""

from datetime import date

from monday_motivation.constants import MONDAY


def is_monday(today: date) -> bool:
    """@brief Tell whether a date is a Monday.

    The date is handed in, so a test can use any day without patching the clock.

    @param today The date to check.
    @return True when the date is a Monday.
    """
    return today.weekday() == MONDAY
