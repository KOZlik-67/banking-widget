
from typing import Any, Dict, List

from src.services import process_bank_operations, process_bank_search


def test_process_bank_search_empty_query() -> None:

    data: List[Dict[str, Any]] = [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    assert process_bank_search(data, "") == data


def test_process_bank_search_found() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "перевод с карты на карту"},
    ]
    result = process_bank_search(data, "перевод")
    assert len(result) == 2
    assert result[0]["id"] == 1
    assert result[1]["id"] == 3


def test_process_bank_search_not_found() -> None:
    data: List[Dict[str, Any]] = [
        {"id": 1, "description": "Перевод организации"}
    ]
    assert process_bank_search(data, "Покупка") == []


def test_process_bank_operations() -> None:
    data: List[Dict[str, Any]] = [
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]
    categories = [
        "Перевод с карты на карту",
        "Открытие вклада",
        "Несуществующая категория",
    ]
    result = process_bank_operations(data, categories)

    assert result["Перевод с карты на карту"] == 2
    assert result["Открытие вклада"] == 1
    assert result["Несуществующая категория"] == 0
