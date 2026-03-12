from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the structure of the incoming data
class CalculationRequest(BaseModel):
    num1: float
    num2: float
    operator: str

@app.post("/calculate")
async def calculate(request: CalculationRequest):
    num1 = request.num1
    num2 = request.num2
    op = request.operator

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero.")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operator. Use +, -, *, or /.")

    return {
        "operation": f"{num1} {op} {num2}",
        "result": result,
    }

@app.get("/hello")
async def hello():
    return {
        "message":"bye"
    }
