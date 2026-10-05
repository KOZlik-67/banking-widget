"""Тестирование функциональности декоратора log."""

from pathlib import Path

import pytest

from src.decorators import log


def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка логирования успешного выполнения в консоль."""

    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "add ok\n" == captured.out


def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверка логирования ошибки в консоль с передачей аргументов."""

    @log()
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(10, y=0)

    captured = capsys.readouterr()
    expected_message = (
        "divide error: ZeroDivisionError. Inputs: (10,), {'y': 0}\n"
    )
    assert captured.out == expected_message


def test_log_file_success(tmp_path: Path) -> None:
    """Проверка логирования успешного выполнения в файл."""
    log_file = tmp_path / "test_success.log"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    result = multiply(4, 5)

    assert result == 20
    assert log_file.read_text(encoding="utf-8").strip() == "multiply ok"


def test_log_file_error(tmp_path: Path) -> None:
    """Проверка логирования ошибки в файл."""
    log_file = tmp_path / "test_error.log"

    @log(filename=str(log_file))
    def failing_func(val: str) -> int:
        return int(val)

    with pytest.raises(ValueError):
        failing_func("not_a_number")

    content = log_file.read_text(encoding="utf-8").strip()
    expected = "failing_func error: ValueError. Inputs: ('not_a_number',), {}"
    assert expected in content
