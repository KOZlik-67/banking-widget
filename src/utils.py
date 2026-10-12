"""Модуль вспомогательных функций для работы с данными транзакций."""

import json
import os
from typing import Any, Dict, List

from src.logger import setup_logger

logger = setup_logger("utils", "utils.log")


def get_transactions_data(file_path: str) -> List[Dict[str, Any]]:
    """Считывает финансовые операции из JSON-файла.

    Возвращает список словарей. Если файл пустой, не найден
    или содержит не список, возвращается пустой список.
    """
    logger.debug(f"Попытка чтения транзакций из файла: {file_path}")

    if not os.path.exists(file_path):
        logger.error(f"Файл не найден по пути: {file_path}")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                logger.info(
                    f"Успешно загружено {len(data)} транзакций из {file_path}"
                )
                return data

            logger.error(
                f"Корень JSON-файла не является списком: получено {type(data)}"
            )
            return []
    except json.JSONDecodeError as err:
        logger.error(f"Ошибка декодирования JSON в файле {file_path}: {err}")
        return []
    except OSError as err:
        logger.error(f"Системная ошибка при чтении файла {file_path}: {err}")
        return []
