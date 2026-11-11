from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Принимает строку с типом и номером карты/счета и возвращает строку с замаскированным номером."""
    name, number = info.rsplit(" ", 1)

    if name.lower().startswith("счет"):
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name.title()} {masked_number}"


def get_date():
    pass


