from src.processing import filter_by_state, sort_by_date
from src.widget import get_date

if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print("Фильтр по умолчанию (EXECUTED):")
    print(filter_by_state(transactions))
    print(filter_by_state(transactions, "CANCELED"))
    print(sort_by_date(transactions))
    print(sort_by_date(transactions, reverse=False))

    formatted_dates = []
    for transaction in transactions:
        current_date = str(transaction["date"])
        formatted_date = get_date(current_date)
        formatted_dates.append(formatted_date)

    print("Список дат:", formatted_dates)
