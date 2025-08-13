from fastapi import FastAPI
from app.routes import expenses

app = FastAPI()

app.include_router(expenses.router, prefix="/expenses", tags=["Expenses"])

@app.get("/")
def read_root():
    return {"message": "Welcome to SplitJi API 🚀"}
