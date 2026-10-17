"""@brief Every constant of the program, in one place.

@file constants.py
"""

from typing import Final

## @brief Subject line of the Monday email.
MAIL_SUBJECT: Final[str] = "Monday Motivation"

## @brief Gmail SMTP server host name.
SMTP_HOST: Final[str] = "smtp.gmail.com"

## @brief Gmail SMTP port that accepts STARTTLS.
SMTP_PORT: Final[int] = 587

## @brief File name of the quote source inside the package data folder.
QUOTES_FILE_NAME: Final[str] = "quotes.txt"

## @brief Encoding of the quote source.
QUOTES_FILE_ENCODING: Final[str] = "utf-8"

## @brief Weekday number of Monday as returned by date.weekday().
MONDAY: Final[int] = 0

## @brief Environment variable that holds the sender address.
ENV_SENDER: Final[str] = "GMAIL_ADDRESS"

## @brief Environment variable that holds the Gmail app password.
ENV_TOKEN: Final[str] = "GMAIL_TOKEN"

## @brief Environment variable that holds the recipient address.
ENV_RECIPIENT: Final[str] = "MONDAY_RECIPIENT"

## @brief Sender shown by a dry run when no sender is configured.
PLACEHOLDER_SENDER: Final[str] = "sender@example.com"

## @brief Recipient shown by a dry run when no recipient is configured.
PLACEHOLDER_RECIPIENT: Final[str] = "recipient@example.com"
