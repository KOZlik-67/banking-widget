"""Главный модуль запуска консольного интерфейса банковского виджета."""

import os
from typing import Any, Dict, List

from src.csv_excel import (
    read_transactions_from_csv,
    read_transactions_from_excel,
)
from src.processing import filter_by_state, sort_by_date
from src.services import process_bank_search
from src.utils import get_transactions_data
from src.widget import get_date, mask_account_card


def get_formatted_amount(operation: Dict[str, Any]) -> str:
    """Извлекает и форматирует сумму и валюту из операции.

    Поддерживает структуры JSON, CSV и XLSX.
    """
    if "operationAmount" in operation:
        amount = operation["operationAmount"].get("amount", "")
        currency = (
            operation["operationAmount"]
            .get("currency", {})
            .get("name", "руб.")
        )
        return f"{amount} {currency}".strip()

    amount = operation.get("amount", "")
    curr_name = operation.get(
        "currency_name", operation.get("currency_code", "руб.")
    )
    return f"{amount} {curr_name}".strip()


def is_rub_transaction(operation: Dict[str, Any]) -> bool:
    """Проверяет, совершена ли операция в рублях."""
    if "operationAmount" in operation:
        code = str(
            operation["operationAmount"].get("currency", {}).get("code", "")
        ).upper()
        return code == "RUB"

    code = str(
        operation.get("currency_code", operation.get("currency_name", ""))
    ).upper()
    return code in ("RUB", "РУБ", "РУБ.")


def print_operations(operations: List[Dict[str, Any]]) -> None:
    """Выводит список банковских операций в форматированном виде."""
    if not operations:
        msg = (
            "Не найдено ни одной транзакции, "
            "подходящей под ваши условия фильтрации"
        )
        print(msg)
        return

    print(f"\nВсего банковских операций в выборке: {len(operations)}\n")
    for op in operations:
        date_str = str(op.get("date", ""))
        formatted_date = get_date(date_str) if date_str else ""
        description = op.get("description", "")

        from_acc = op.get("from")
        to_acc = op.get("to")

        from_masked = mask_account_card(str(from_acc)) if from_acc else ""
        to_masked = mask_account_card(str(to_acc)) if to_acc else ""

        print(f"{formatted_date} {description}")
        if from_masked and to_masked:
            print(f"{from_masked} -> {to_masked}")
        elif to_masked:
            print(to_masked)
        elif from_masked:
            print(from_masked)

        amount_info = get_formatted_amount(op)
        print(f"Сумма: {amount_info}\n")


def main() -> None:
    """Основная логика взаимодействия с пользователем."""
    greeting = (
        "Привет! Добро пожаловать в программу "
        "работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )
    print(greeting)

    user_choice = input().strip()
    project_root = os.path.dirname(os.path.abspath(__file__))

    transactions: List[Dict[str, Any]] = []
    if user_choice == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_transactions_data(
            os.path.join(project_root, "data", "operations.json")
        )
    elif user_choice == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_transactions_from_csv(
            os.path.join(project_root, "data", "transactions.csv")
        )
    elif user_choice == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_transactions_from_excel(
            os.path.join(project_root, "data", "transactions_excel.xlsx")
        )
    else:
        print("Неверный пункт меню.")
        return

    valid_statuses = ("EXECUTED", "CANCELED", "PENDING")
    while True:
        print("\nВведите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip()
        status_upper = status.upper()

        if status_upper in valid_statuses:
            print(f'Операции отфильтрованы по статусу "{status_upper}"')
            transactions = filter_by_state(transactions, status_upper)
            break
        print(f'Статус операции "{status}" недоступен.')

    print("\nОтсортировать операции по дате? Да/Нет")
    if input().strip().lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().strip().lower()
        sorted_tx = sort_by_date(transactions)
        if order == "по возрастанию":
            transactions = list(reversed(sorted_tx))
        else:
            transactions = sorted_tx

    print("\nВыводить только рублевые транзакции? Да/Нет")
    if input().strip().lower() == "да":
        transactions = [op for op in transactions if is_rub_transaction(op)]

    search_prompt = (
        "\nОтфильтровать список транзакций по определенному слову "
        "в описании? Да/Нет"
    )
    print(search_prompt)
    if input().strip().lower() == "да":
        print("Введите строку для поиска:")
        search_query = input().strip()
        transactions = process_bank_search(transactions, search_query)

    print("\nРаспечатываю итоговый список транзакций...")
    print_operations(transactions)


if __name__ == "__main__":
    main()
