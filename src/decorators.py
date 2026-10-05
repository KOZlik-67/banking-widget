"""Модуль, содержащий декораторы для функций проекта."""

import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор для логирования выполнения функции и обработки ошибок """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            def write_log(message: str) -> None:
                """Записывает сообщение в файл или выводит в консоль."""
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")
                else:
                    print(message)

            try:
                result = func(*args, **kwargs)
                write_log(f"{func.__name__} ok")
                return result
            except Exception as e:
                # В тексте задания формат: <name> error: <тип ошибки>. Inputs: (<args>), {<kwargs>}
                error_msg = f"{func.__name__} error: {e.__class__.__name__}. Inputs: {args}, {kwargs}"
                write_log(error_msg)
                raise e

        return wrapper

    return decorator
