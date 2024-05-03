from fastapi import FastAPI
from app.model import predict_pipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/predict/{input}")
def read_item(input: str):
    result = predict_pipeline(input)
    return {"emotion": result}
