"""Тестирование инициализации и настройки логеров."""

import logging
from pathlib import Path

from src.logger import setup_logger


def test_setup_logger(tmp_path: Path) -> None:
    """Проверка создания логера, хэндлера и формата записи."""
    test_logger = setup_logger("test_module", "test.log")

    assert test_logger.name == "test_module"
    assert test_logger.level == logging.DEBUG
    assert len(test_logger.handlers) >= 1

    handler = test_logger.handlers[0]
    assert isinstance(handler, logging.FileHandler)
    assert handler.level == logging.DEBUG
    assert handler.formatter is not None
