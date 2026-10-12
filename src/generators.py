from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency: str
) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по заданной валюте."""
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        curr = operation_amount.get("currency", {})
        if curr.get("code") == currency:
            yield transaction


def transaction_descriptions(
    transactions: List[Dict[str, Any]]
) -> Iterator[str]:
    """Возвращает описание каждой ."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера банковских карт ."""
    for number in range(start, stop + 1):
        num_str = f"{number:016d}"
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:]}"
