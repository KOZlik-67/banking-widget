from src.widget import get_date, mask_account_card

test_cases = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

for item in test_cases:
    print(mask_account_card(item))

print(get_date("2024-03-11T02:26:18.671407"))