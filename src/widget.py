from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data: str) -> str:

    if not isinstance(data, str) or not data.strip():
        return ""

    parts = data.strip().split()
    if len(parts) < 2:
        return data

    name = " ".join(parts[:-1])
    number = parts[-1]

    if not number.isdigit():
        return data

    if name.lower().startswith("счет") or name.lower().startswith("счёт"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_str: str) -> str:

    parsed_date = datetime.fromisoformat(date_str)
    return parsed_date.strftime("%d.%m.%Y")
