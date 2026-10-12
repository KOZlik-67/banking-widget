"""Тестирование модуля конвертации валют через API."""

from unittest.mock import Mock, patch

import requests

from src.external_api import convert_to_rubles


def test_convert_to_rubles_rub() -> None:
    """Проверка возврата суммы для транзакции в RUB без обращения к API."""
    transaction = {
        "operationAmount": {
            "amount": "1500.50",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rubles(transaction) == 1500.50


@patch("src.external_api.requests.get")
def test_convert_to_rubles_usd_success(mock_get: Mock) -> None:
    """Проверка успешной конвертации USD через API."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 8500.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"},
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 8500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rubles_eur_success(mock_get: Mock) -> None:
    """Проверка успешной конвертации EUR через API."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 9200.75}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "EUR"},
        }
    }
    result = convert_to_rubles(transaction)
    assert result == 9200.75
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rubles_request_exception(mock_get: Mock) -> None:
    """Проверка возврата 0.0 при возникновении сетевой ошибки."""
    mock_get.side_effect = requests.RequestException("Connection error")

    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "USD"},
        }
    }
    assert convert_to_rubles(transaction) == 0.0


@patch("src.external_api.requests.get")
def test_convert_to_rubles_no_result_in_response(mock_get: Mock) -> None:
    """Проверка случая, когда API вернул ответ без поля result."""
    mock_response = Mock()
    mock_response.json.return_value = {"success": False}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "50.0",
            "currency": {"code": "USD"},
        }
    }
    assert convert_to_rubles(transaction) == 0.0


def test_convert_to_rubles_unsupported_currency() -> None:
    """Проверка возврата 0.0 для неподдерживаемой валюты (например, GBP)."""
    transaction = {
        "operationAmount": {
            "amount": "20.0",
            "currency": {"code": "GBP"},
        }
    }
    assert convert_to_rubles(transaction) == 0.0


def test_convert_to_rubles_invalid_amount() -> None:
    """Проверка обработки некорректного значения amount."""
    transaction = {
        "operationAmount": {
            "amount": "invalid_num",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rubles(transaction) == 0.0


def test_convert_to_rubles_empty_transaction() -> None:
    """Проверка обработки пустого словаря транзакции."""
    assert convert_to_rubles({}) == 0.0
