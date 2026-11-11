def get_mask_card_number(card_number: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску в формате XXXX XX** **** XXXX."""
    clean_number = card_number.replace(" ", "")

    if not clean_number.isdigit() or len(clean_number) != 16:
        raise ValueError("Номер карты должен состоять строго из 16 цифр")

    return f"{clean_number[:4]} {clean_number[4:6]}** **** {clean_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Принимает на вход номер счета и возвращает его маску в формате **XXXX."""
    clean_account = account_number.replace(" ", "")

    if not clean_account.isdigit() or len(clean_account) < 4:
        raise ValueError("Номер счета должен состоять из цифр и содержать не менее 4 символов")

    return f"**{clean_account[-4:]}"
