"""Модуль дополнительных сервисов обработки банковских транзакций."""

import re
from collections import Counter
from typing import Any, Dict, List


def process_bank_search(
    data: List[Dict[str, Any]], search: str
) -> List[Dict[str, Any]]:

    if not search:
        return data
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    matched_transactions: List[Dict[str, Any]] = []

    for item in data:
        description = str(item.get("description", ""))
        if pattern.search(description):
            matched_transactions.append(item)

    return matched_transactions


def process_bank_operations(
    data: List[Dict[str, Any]], categories: List[str]
) -> Dict[str, int]:

    descriptions = [
        str(item.get("description", ""))
        for item in data
        if "description" in item
    ]
    counts = Counter(descriptions)

    return {category: counts.get(category, 0) for category in categories}
