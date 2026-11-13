from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def main() -> None:
    """Точка входа для демонстрации работы функций проекта."""
    while True:
        user_input = input(
            "\nВведите данные (Visa 1234567812345678, Счет 1234567890... " "или exit для выхода): "
        ).strip()

        if user_input.lower() == "exit":
            print("Программа завершена.")
            break

        if user_input == "":
            print("Строка не должна быть пустой. Попробуйте еще раз.")
            continue

        result = mask_account_card(user_input)
        if result.startswith("Ошибка:"):
            print(result)
        else:
            print(f"Результат: {result}")
            break

    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print("\nФильтр по умолчанию (EXECUTED):")
    print(filter_by_state(transactions))
    print(filter_by_state(transactions, "CANCELED"))
    print(sort_by_date(transactions))
    print(sort_by_date(transactions, reverse=False))

    formatted_dates = [get_date(str(transaction["date"])) for transaction in transactions]
    print("Список дат:", formatted_dates)


if __name__ == "__main__":
    main()
