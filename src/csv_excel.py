"""Модуль считывания финансовых транзакций из CSV и Excel (XLSX) файлов."""

import os
from typing import Any, Dict, List, cast

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из CSV-файла.

    :param file_path: Путь к CSV-файлу.
    :return: Список словарей с финансовыми транзакциями.
             Если файл не найден или поврежден, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path, sep=";", encoding="utf-8")
        if df.empty:
            return []
        records = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return records
    except Exception:
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из файла Excel (.xlsx).

    :param file_path: Путь к файлу Excel.
    :return: Список словарей с финансовыми транзакциями.
             Если файл не найден или поврежден, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_excel(file_path)
        if df.empty:
            return []
        records = cast(List[Dict[str, Any]], df.to_dict(orient="records"))
        return records
    except Exception:
        return []