def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате XXXX XX** **** XXXX."""
    clean_number = str(card_number).replace(" ", "")
    if len(clean_number) < 16:
        return clean_number
    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **XXXX."""
    clean_account = str(account_number).strip()
    if len(clean_account) < 4:
        return clean_account
    return f"**{clean_account[-4:]}"
