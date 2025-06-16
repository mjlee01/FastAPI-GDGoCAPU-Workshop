from fastapi import FastAPI
from typing import Optional

# request with body
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi import status

# request with headers
from fastapi import Header, HTTPException

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "Welcome to McDonalds!"}

# path parameter
@app.get("/greet/{name}")
async def greet_user(name: str) -> dict:
    return {"message": f"Hi {name}, Welcome to McDonalds!"}

# query parameter
@app.get("/greet")
async def greet_user_with_restaurant(name: str, restaurant: str) -> dict:
    return {"message": f"Hi {name}, Welcome to {restaurant}!"}

# path and query parameter (mix)
@app.get("/profile/{name}")
async def get_profile(name: str, phone_no: int) -> dict:
    return {"profile": {"name": name, "phone_number": phone_no}}

# optional query parameters (with default values)
@app.get("/points/{name}")
async def get_points(name: str, points: Optional[int] = 0) -> dict:
    return {"message": f"Hi {name}, your current have {points} points!"}

# order create schema
class OrderCreateModel(BaseModel):
    id: UUID = None
    main: str
    side: Optional[str] = None
    drink: Optional[str] = None
    quantity: int
    price: float
    status: str = "preparing"

# create order
@app.post("/order", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreateModel) -> dict:
    # generate a unique ID for the order
    order.id = uuid4()
    return {
        "message": f"Your order for {order.main} has been placed successfully!",
        "order_details": order,
    }

# order update schema
class OrderUpdateModel(BaseModel):
    id: UUID
    status: str

# update order status
@app.patch("/staff/update-order-status")
async def update_order_status(
    update_data: OrderUpdateModel,
    staff_name: Optional[str] = Header(None),
) -> dict:
    staffs = ["Rudory", "Sharky", "Baobao"]
    if not staff_name or staff_name not in staffs:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Only staff can update order"
        )

    return {
        "message": f"Order {update_data.id} has been updated by staff!",
        "new_order_status": update_data.status,
        "updated_by": staff_name,
    }