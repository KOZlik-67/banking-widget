import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79** **** 6361"),
        ("МИР 7000792289606361", "МИР 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("", ""),
        ("   ", ""),
        ("CardOnly", "CardOnly"),
        ("Visa Platinum number", "Visa Platinum number"),
    ],
)
def test_mask_account_card(input_data: str, expected: str) -> None:
    """Тестирование маскирования карт и счетов с параметризацией."""
    assert mask_account_card(input_data) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T12:00:00", "11.07.2018"),
        ("2026-09-21T13:00:00.000", "21.09.2026"),
    ],
)
def test_get_date(date_str: str, expected: str) -> None:
    """Тестирование корректного преобразования дату."""
    assert get_date(date_str) == expected


def test_get_date_invalid() -> None:
    """Проверка возбуждения ошибки при некорректном   даты."""
    with pytest.raises(ValueError):
        get_date("invalid-date-string")