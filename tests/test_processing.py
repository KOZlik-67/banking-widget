from typing import Any, Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование фильтрации со значением state по умолчанию."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_canceled(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование фильтрации по статусу CANCELED."""
    result = filter_by_state(sample_transactions, state="CANCELED")
    assert len(result) == 2
    assert all(item["state"] == "CANCELED" for item in result)


def test_filter_by_state_empty(
    empty_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование фильтрации на пустом списке."""
    assert filter_by_state(empty_transactions) == []


def test_sort_by_date_descending(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование сортировки по дате по убыванию."""
    result = sort_by_date(sample_transactions)
    assert result[0]["id"] == 41428829
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование сортировки по дате по возрастанию."""
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["id"] == 939719570
    assert result[-1]["id"] == 41428829


def test_sort_by_date_empty(
    empty_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование сортировки на пустом списке."""
    assert sort_by_date(empty_transactions) == []
