import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card_visa() -> None:
    """Тестирование маскировки номера карты Visa."""
    card = "Visa Platinum 7000792289606361"
    assert mask_account_card(card) == "Visa Platinum 7000 79** **** 6361"


def test_mask_account_card_account() -> None:
    """Тестирование маскировки номера счета."""
    account = "Счет 73654108430135874305"
    assert mask_account_card(account) == "Счет **4305"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account_card_parametrize(value: str, expected: str) -> None:
    """Параметризованный тест для карт и счетов."""
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
    ],
)
def test_get_date(date_string: str, expected: str) -> None:
    """Тестирование форматирования даты."""
    assert get_date(date_string) == expected
