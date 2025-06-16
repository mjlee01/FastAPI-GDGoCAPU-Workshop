from pydantic import BaseModel
from enum import Enum


class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"


class AccountType(str, Enum):
    TNG = "TNG"
    BANK = "Bank"
    CASH = "Cash"


class TransactionResponseModel(BaseModel):
    id: int
    type: str
    amount: float
    date: str
    description: str
    category: str
    account: str


class TransactionCreateModel(BaseModel):
    type: TransactionType
    amount: float
    description: str
    category: str
    account: AccountType


class BalanceResponseModel(BaseModel):
    account: str
    total_income: float
    total_expense: float
    net_balance: float
    transaction_count: int


class BalanceSummaryResponseModel(BaseModel):
    total_income: float
    total_expense: float
    net_balance: float
    transaction_count: int
    accounts: dict[str, BalanceResponseModel]