from fastapi import FastAPI

HELLO_WORLD = {"msg": "Hello, World!"}

app = FastAPI()


@app.get("/")
async def root():
    return HELLO_WORLD
