import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000 7922 8960 6361", "7000 79** **** 6361"),
        ("12345", "12345"),
        ("", ""),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str) -> None:
    """Тестирование маскирования номеров  ."""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
        ("123", "123"),
        ("", ""),
        (" 73654108430135874305 ", "**4305"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    """Тестирование маскирования номеров счетов   ."""
    assert get_mask_account(account_number) == expected
