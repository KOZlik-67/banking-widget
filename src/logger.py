"""Модуль настройки логеров для компонентов приложения."""

import logging
from pathlib import Path


def setup_logger(name: str, log_filename: str) -> logging.Logger:
    """Настраивает и возвращает логер с записью в файл.

    :param name: Имя логера (название модуля).
    :param log_filename: Имя файла лога (например, 'masks.log').
    :return: Настроенный объект Logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        project_root = Path(__file__).resolve().parent.parent
        log_dir = project_root / "logs"
        log_dir.mkdir(exist_ok=True)
        log_file_path = log_dir / log_filename

        file_handler = logging.FileHandler(
            log_file_path, mode="w", encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)

        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        logger.addHandler(file_handler)

    return logger
