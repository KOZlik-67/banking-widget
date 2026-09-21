# Banking Operations Widget

Виджет для личного кабинета клиента банка, подготавливающий данные для отображения банковских операций.

## Описание модулей и функций

### Модуль `masks`
* `get_mask_card_number(card_number)` — маскирует номер карты (`XXXX XX** **** XXXX`).
* `get_mask_account(account_number)` — маскирует номер счета (`**XXXX`).

### Модуль `widget`
* `mask_account_card(data)` — определяет карту или счет и возвращает замаскированный номер.
* `get_date(date_str)` — преобразует ISO-дату в формат `ДД.ММ.ГГГГ`.

### Модуль `processing`
* `filter_by_state(data, state="EXECUTED")` — фильтрует список словарей операций по статусу.
* `sort_by_date(data, descending=True)` — сортирует операции по дате (по умолчанию от новых к старым).

## Установка и запуск

1. Клонировать репозиторий:
```bash
git clone [https://github.com/KOZlik-67/banking-widget.git](https://github.com/KOZlik-67/banking-widget.git)
```
2. Установить зависимости:
```bash
poetry install
```