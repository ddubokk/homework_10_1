def filter_by_state(transactions: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует список банковских операций по заданному статусу."""
    filtered_transactions = []
    for transaction in transactions:
        if transaction.get("state") == state:
            filtered_transactions.append(transaction)
    return filtered_transactions


def sort_by_date(transactions: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует список по дате."""
    return sorted(transactions, key=lambda transaction: transaction["date"], reverse=reverse)
