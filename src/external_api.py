"""Модуль конвертации валют транзакций через внешний API."""

import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rubles(transaction: Dict[str, Any]) -> float:
    """Конвертирует сумму операции в рубли (RUB).

    Если валюта операции указана как USD или EUR,
    запрашивает актуальный курс через Exchange Rates Data API.
    Для операций в рублях возвращает сумму без запроса к API.
    """
    operation_amount = transaction.get("operationAmount", {})
    amount_str = operation_amount.get("amount", "0")
    try:
        amount = float(amount_str)
    except (ValueError, TypeError):
        return 0.0

    currency_code = (
        operation_amount.get("currency", {}).get("code", "").upper()
    )

    if currency_code == "RUB":
        return amount

    if currency_code in ("USD", "EUR"):
        api_key: str = os.getenv("API_KEY") or ""
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"from": currency_code, "to": "RUB", "amount": str(amount)}
        headers: Dict[str, str] = {"apikey": api_key}

        try:
            response = requests.get(
                url, params=params, headers=headers, timeout=10
            )
            response.raise_for_status()
            data = response.json()
            result = data.get("result")
            if result is not None:
                return float(result)
        except requests.RequestException:
            return 0.0

    return 0.0
