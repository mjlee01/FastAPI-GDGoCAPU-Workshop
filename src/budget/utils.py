from transactions import transactions
from schema import TransactionCreateModel, AccountType
from datetime import datetime


def get_next_id():
    return max(t["id"] for t in transactions) + 1 if transactions else 1


def get_date():
    return datetime.now().date()


def add_transaction(transaction_data: TransactionCreateModel):
    new_transaction = {
        "id": get_next_id(),
        "date": str(get_date()),
        **transaction_data.model_dump(),
    }
    transactions.append(new_transaction)
    return new_transaction


def get_all_transactions():
    return transactions


def get_transaction_by_id(id: int):
    for t in transactions:
        if t["id"] == id:
            return t
    return None


def update_transaction_by_id(id: int, update_data: TransactionCreateModel):
    transaction = get_transaction_by_id(id)
    if transaction:
        transaction.update(update_data)
        return transaction
    return None


def delete_transaction_by_id(id: int):
    global transactions
    transactions = [t for t in transactions if t["id"] != id]
    return transactions


def calculate_account_balance(account: AccountType):
    account_transactions = [t for t in transactions if t["account"] == account]

    total_income = sum(
        t["amount"] for t in account_transactions if t["type"] == "income"
    )
    total_expense = sum(
        t["amount"] for t in account_transactions if t["type"] == "expense"
    )
    net_balance = total_income - total_expense

    return {
        "account": account,
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance,
        "transaction_count": len(account_transactions),
    }


def calculate_overall_balance():
    total_income = sum(t["amount"] for t in transactions if t["type"] == "income")
    total_expense = sum(t["amount"] for t in transactions if t["type"] == "expense")
    net_balance = total_income - total_expense

    accounts = set(t["account"] for t in transactions)
    account_balances = {
        account: calculate_account_balance(account) for account in accounts
    }

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance,
        "transaction_count": len(transactions),
        "accounts": account_balances,
    }