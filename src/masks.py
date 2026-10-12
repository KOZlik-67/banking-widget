"""Модуль маскирования номеров банковских карт и счетов."""

from src.logger import setup_logger

logger = setup_logger("masks", "masks.log")


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формат XXXX XX** **** XXXX."""
    logger.debug(f"Начало маскирования номера карты: {card_number}")
    digits = card_number.replace(" ", "")

    if not digits.isdigit() or len(digits) != 16:
        logger.error(
            f"Некорректный номер карты: {card_number}. Ожидается 16 цифр."
        )
        return card_number

    masked = f"{digits[:4]} {digits[4:6]}** **** {digits[12:]}"
    logger.info(f"Номер карты успешно замаскирован: {masked}")
    return masked


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формат **XXXX."""
    logger.debug(f"Начало маскирования номера счета: {account_number}")
    digits = account_number.replace(" ", "")

    if not digits.isdigit() or len(digits) < 4:
        logger.error(
            f"Некорректный номер счета: {account_number}. Минимум 4 цифры."
        )
        return account_number

    masked = f"**{digits[-4:]}"
    logger.info(f"Номер счета успешно замаскирован: {masked}")
    return masked
