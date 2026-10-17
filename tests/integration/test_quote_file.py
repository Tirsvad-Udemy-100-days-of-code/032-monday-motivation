from pathlib import Path

import pytest

from monday_motivation.domain.errors import NoQuotesError, QuotesFileError
from monday_motivation.infrastructure.quote_file import (
    DEFAULT_QUOTES_PATH,
    read_quotes,
)

MINIMUM_PACKAGED_QUOTES = 100


def test_read_quotes_skips_blank_lines_and_keeps_curly_quotes(
    tmp_path: Path,
) -> None:
    path = tmp_path / "quotes.txt"
    path.write_text("“First”\n\n   \nSecond\n", encoding="utf-8", newline="\n")
    assert read_quotes(path) == ["“First”", "Second"]


def test_read_quotes_raises_for_missing_file(tmp_path: Path) -> None:
    with pytest.raises(QuotesFileError) as info:
        read_quotes(tmp_path / "missing.txt")
    assert isinstance(info.value.__cause__, OSError)


def test_read_quotes_raises_for_empty_file(tmp_path: Path) -> None:
    path = tmp_path / "quotes.txt"
    path.write_text("\n  \n", encoding="utf-8")
    with pytest.raises(NoQuotesError):
        read_quotes(path)


def test_read_quotes_packaged_file_holds_at_least_100_quotes() -> None:
    quotes = read_quotes(DEFAULT_QUOTES_PATH)
    assert len(quotes) >= MINIMUM_PACKAGED_QUOTES
    assert all(quote.strip() for quote in quotes)
