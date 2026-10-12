from typing import Any, Dict, List

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


def test_filter_by_currency_usd(
    transactions_with_currencies: List[Dict[str, Any]]
) -> None:
    """Тест фильтрации по валюте USD."""
    gen = filter_by_currency(transactions_with_currencies, "USD")
    first = next(gen)
    second = next(gen)
    assert first["id"] == 939719570
    assert second["id"] == 142264268
    with pytest.raises(StopIteration):
        next(gen)


def test_filter_by_currency_not_found(
    transactions_with_currencies: List[Dict[str, Any]]
) -> None:
    """Тест при отсутствии транзакций с указанной валютой."""
    gen = filter_by_currency(transactions_with_currencies, "EUR")
    with pytest.raises(StopIteration):
        next(gen)


def test_filter_by_currency_empty() -> None:
    """Тест фильтрации на пустом списке."""
    gen = filter_by_currency([], "USD")
    with pytest.raises(StopIteration):
        next(gen)


def test_transaction_descriptions(
    transactions_with_currencies: List[Dict[str, Any]]
) -> None:
    """Тест возврата описания для каждой операции."""
    gen = transaction_descriptions(transactions_with_currencies)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    with pytest.raises(StopIteration):
        next(gen)


def test_transaction_descriptions_empty() -> None:
    """Тест описаний на пустом списке."""
    gen = transaction_descriptions([])
    with pytest.raises(StopIteration):
        next(gen)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1,
            2,
            ["0000 0000 0000 0001", "0000 0000 0000 0002"],
        ),
        (
            9999999999999998,
            9999999999999999,
            ["9999 9999 9999 9998", "9999 9999 9999 9999"],
        ),
        (
            5,
            5,
            ["0000 0000 0000 0005"],
        ),
    ],
)
def test_card_number_generator(
    start: int, stop: int, expected: List[str]
) -> None:
    """Тестирование генератора номеров карт и формата строк."""
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_invalid_range() -> None:
    """Тест при некорректном диапазоне (start > stop)."""
    assert list(card_number_generator(5, 1)) == []
