from fastapi import FastAPI, HTTPException, status
from schema import (
    TransactionResponseModel,
    TransactionCreateModel,
    AccountType,
    BalanceResponseModel,
    BalanceSummaryResponseModel,
)
from utils import (
    add_transaction,
    get_all_transactions,
    get_transaction_by_id,
    update_transaction_by_id,
    delete_transaction_by_id,
    calculate_account_balance,
    calculate_overall_balance,
)
from typing import List

app = FastAPI()

@app.get(
    "/transactions",
    response_model=List[TransactionResponseModel],
    status_code=status.HTTP_200_OK,
)
async def get_transactions():
    return get_all_transactions()

@app.get(
    "/transaction/{id}",
    response_model=TransactionResponseModel,
    status_code=status.HTTP_200_OK,
)
async def get_transaction(id: int):
    transaction = get_transaction_by_id(id)
    if not transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with ID {id} not found.",
        )
    return transaction

@app.post(
    "/transaction",
    status_code=status.HTTP_201_CREATED,
    response_model=TransactionResponseModel,
)
async def create_transaction(txn: TransactionCreateModel):
    new_transaction = add_transaction(txn)
    return new_transaction

@app.patch(
    "/transaction/{id}",
    response_model=TransactionResponseModel,
    status_code=status.HTTP_200_OK,
)
async def update_transaction(id: int, update_data: TransactionCreateModel):
    updated_transaction = update_transaction_by_id(id, update_data)
    if not updated_transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with ID {id} not found.",
        )
    return updated_transaction

@app.delete(
    "/transaction/{id}",
    response_model=List[TransactionResponseModel],
    status_code=status.HTTP_200_OK,
)
async def delete_transaction(id: int):
    deleted_transaction = delete_transaction_by_id(id)
    if not deleted_transaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Transaction with id {id} not found",
        )
    return deleted_transaction

@app.get(
    "/balance/{account}",
    response_model=BalanceResponseModel,
    status_code=status.HTTP_200_OK,
)
async def get_account_balance(account: AccountType):
    result = calculate_account_balance(account)
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No transactions found for account {account}",
        )
    return result

    
@app.get(
    "/balance",
    response_model=BalanceSummaryResponseModel,
    status_code=status.HTTP_200_OK,
)
async def get_overall_balance():
    result = calculate_overall_balance()
    return result