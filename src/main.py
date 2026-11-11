from src.masks import get_mask_account, get_mask_card_number

if __name__ == "__main__":
    # 1. Проверяем маску карты
    card_input = input("Введите номер карты: ")
    print(f"Маска карты: {get_mask_card_number(card_input)}")

    print("-" * 40)
    print("*" * 40)

    # 2. Проверяем маску счета
    account_input = input("Введите номер счета: ")
    print(f"Маска счета: {get_mask_account(account_input)}")
