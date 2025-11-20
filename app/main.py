from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, CI/CD World!"}

@app.get("/predict")
def predict(x: int, y: int):
    return {"result": x + y}
