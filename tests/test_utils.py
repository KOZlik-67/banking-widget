"""Тестирование функции чтения финансовых операций из JSON."""

import json
from unittest.mock import mock_open, patch

from src.utils import get_transactions_data


def test_get_transactions_data_success() -> None:
    """Проверка успешной загрузки списка транзакций."""
    mock_json = json.dumps([{"id": 1, "state": "EXECUTED"}])
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_json)):
            result = get_transactions_data("dummy.json")
            assert result == [{"id": 1, "state": "EXECUTED"}]


def test_get_transactions_data_file_missing() -> None:
    """Проверка поведения при отсутствии целевого файла."""
    with patch("os.path.exists", return_value=False):
        assert get_transactions_data("non_existing.json") == []


def test_get_transactions_data_not_a_list() -> None:
    """Проверка случая, когда корень JSON является объектом, а не списком."""
    mock_json = json.dumps({"key": "value"})
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=mock_json)):
            assert get_transactions_data("dict.json") == []


def test_get_transactions_data_invalid_json() -> None:
    """Проверка обработки некорректного или битого JSON."""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data="{broken json")):
            assert get_transactions_data("invalid.json") == []
