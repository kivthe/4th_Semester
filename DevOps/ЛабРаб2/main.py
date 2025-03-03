from fastapi import FastAPI, HTTPException

app = FastAPI()

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n: int) -> int:
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

def fibonacci(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

@app.get("/prime/{n}")
async def get_nth_prime(n: int):
    if n < 1:
        raise HTTPException(status_code=400, detail="N must be a positive integer.")
    return {"nth_prime": nth_prime(n)}

@app.get("/fibonacci/{n}")
async def get_nth_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="N must be a non-negative integer.")
    return {"nth_fibonacci": fibonacci(n)}