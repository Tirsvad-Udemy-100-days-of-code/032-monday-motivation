"""@brief Errors raised by Monday Motivation.

@file errors.py
"""


class MondayMotivationError(Exception):
    """@brief Base class of every error the program raises on purpose."""


class NoQuotesError(MondayMotivationError):
    """@brief There is no quote to choose from."""


class QuotesFileError(MondayMotivationError):
    """@brief The quote source could not be read."""


class MissingSettingError(MondayMotivationError):
    """@brief A required environment variable is not set."""


class MailSendError(MondayMotivationError):
    """@brief The email could not be sent."""
