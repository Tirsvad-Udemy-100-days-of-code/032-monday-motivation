"""@brief Reading the quote source.

@file quote_file.py
"""

from pathlib import Path

from monday_motivation.constants import QUOTES_FILE_ENCODING, QUOTES_FILE_NAME
from monday_motivation.domain.errors import NoQuotesError, QuotesFileError

DEFAULT_QUOTES_PATH = Path(__file__).parent / "data" / QUOTES_FILE_NAME


def read_quotes(path: Path = DEFAULT_QUOTES_PATH) -> list[str]:
    """@brief Read the quotes, one per line, skipping blank lines.

    @param path The quote source; the packaged quotes file by default.
    @return The quotes in file order.
    @raises QuotesFileError When the file cannot be read.
    @raises NoQuotesError When the file holds no quote.
    """
    try:
        with path.open(encoding=QUOTES_FILE_ENCODING) as quote_file:
            quotes = [line.strip() for line in quote_file if line.strip()]
    except OSError as error:
        raise QuotesFileError(f"Cannot read the quotes file {path}.") from error
    if not quotes:
        raise NoQuotesError(f"The quotes file {path} holds no quote.")
    return quotes
