# Banking Widget

Виджет для обработки и фильтрации банковских операций клиента.

## Модуль генераторов (`src/generators.py`)

Модуль предназначен для эффективной обработки массивов транзакций с помощью итераторов и генераторов Python.

### Основные функции:

1. **`filter_by_currency(transactions, currency)`**  
   Фильтрует список транзакций по заданной валюте (например, `"USD"`, `"RUB"`) и возвращает итератор.
   ```python
   usd_transactions = filter_by_currency(transactions, "USD")
   print(next(usd_transactions))
 

card_number_generator(start, stop)

Генерирует номера банковских карт формата XXXX XXXX XXXX XXXX в заданном диапазоне.
  ```python
  for card in card_number_generator(1, 5):
    print(card)
  
transaction_descriptions(transactions)

Генератор текстовых описаний операций по очереди.
   ```python
descriptions = transaction_descriptions(transactions)
print(next(descriptions))
