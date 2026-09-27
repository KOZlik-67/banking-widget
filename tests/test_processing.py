from typing import Any, Dict, List
import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование фильтрации со значением state по умолчанию."""
    result = filter_by_state(sample_transactions)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


@pytest.mark.parametrize(
    "state, expected_count",
    [
        ("EXECUTED", 2),
        ("CANCELED", 2),
        ("PENDING", 0),
    ],
)
def test_filter_by_state_param(
    sample_transactions: List[Dict[str, Any]], state: str, expected_count: int
) -> None:
    """Параметризованный тест фильтрации по разным состояниям."""
    result = filter_by_state(sample_transactions, state=state)
    assert len(result) == expected_count


def test_filter_by_state_empty(
    empty_transactions: List[Dict[str, Any]],
) -> None:
    """Тест фильтрации на пустом списке."""
    assert filter_by_state(empty_transactions) == []


def test_sort_by_date_descending(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование сортировки по дате по убыванию."""
    result = sort_by_date(sample_transactions, descending=True)
    assert result[0]["id"] == 41428829
    assert result[-1]["id"] == 939719570


def test_sort_by_date_ascending(
    sample_transactions: List[Dict[str, Any]],
) -> None:
    """Тестирование сортировки по дате по возрастанию."""
    result = sort_by_date(sample_transactions, descending=False)
    assert result[0]["id"] == 939719570
    assert result[-1]["id"] == 41428829


def test_sort_by_date_empty(empty_transactions: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки на пустом списке."""
    assert sort_by_date(empty_transactions) == []

