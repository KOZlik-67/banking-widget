"""Тестирование модуля чтения данных из CSV и Excel файлов."""

from typing import Any, Dict, List
from unittest.mock import Mock, patch

import pandas as pd

from src.csv_excel import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)


def test_read_csv_file_not_found() -> None:
    """Проверка возврата пустого списка, если CSV-файл не существует."""
    with patch("os.path.exists", return_value=False):
        assert read_transactions_from_csv("non_existent.csv") == []


@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv")
def test_read_csv_success(
    mock_read_csv: Mock, mock_exists: Mock
) -> None:
    """Проверка успешного считывания операций из CSV."""
    raw_data: List[Dict[str, Any]] = [
        {"id": 1, "amount": 100.0, "currency": "RUB"},
        {"id": 2, "amount": 250.5, "currency": "USD"},
    ]
    mock_df = pd.DataFrame(raw_data)
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("dummy.csv")
    assert result == raw_data
    mock_read_csv.assert_called_once_with(
        "dummy.csv", sep=";", encoding="utf-8"
    )


@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv")
def test_read_csv_empty_dataframe(
    mock_read_csv: Mock, mock_exists: Mock
) -> None:
    """Проверка возврата пустого списка при пустом DataFrame из CSV."""
    mock_read_csv.return_value = pd.DataFrame()
    assert read_transactions_from_csv("empty.csv") == []


@patch("os.path.exists", return_value=True)
@patch("pandas.read_csv")
def test_read_csv_exception(
    mock_read_csv: Mock, mock_exists: Mock
) -> None:
    """Проверка обработки исключений при чтении битого CSV-файла."""
    mock_read_csv.side_effect = Exception("Parsing error")
    assert read_transactions_from_csv("corrupted.csv") == []


def test_read_excel_file_not_found() -> None:
    """Проверка возврата пустого списка, если Excel-файл не существует."""
    with patch("os.path.exists", return_value=False):
        assert read_transactions_from_excel("non_existent.xlsx") == []


@patch("os.path.exists", return_value=True)
@patch("pandas.read_excel")
def test_read_excel_success(
    mock_read_excel: Mock, mock_exists: Mock
) -> None:
    """Проверка успешного считывания операций из Excel."""
    raw_data: List[Dict[str, Any]] = [
        {"id": 10, "amount": 5000.0, "currency": "RUB"},
        {"id": 20, "amount": 12.0, "currency": "EUR"},
    ]
    mock_df = pd.DataFrame(raw_data)
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("dummy.xlsx")
    assert result == raw_data
    mock_read_excel.assert_called_once_with("dummy.xlsx")


@patch("os.path.exists", return_value=True)
@patch("pandas.read_excel")
def test_read_excel_empty_dataframe(
    mock_read_excel: Mock, mock_exists: Mock
) -> None:
    """Проверка возврата пустого списка при пустом DataFrame из Excel."""
    mock_read_excel.return_value = pd.DataFrame()
    assert read_transactions_from_excel("empty.xlsx") == []


@patch("os.path.exists", return_value=True)
@patch("pandas.read_excel")
def test_read_excel_exception(
    mock_read_excel: Mock, mock_exists: Mock
) -> None:
    """Проверка обработки исключений при чтении поврежденного Excel-файла."""
    mock_read_excel.side_effect = Exception("Read excel error")
    assert read_transactions_from_excel("corrupted.xlsx") == []
