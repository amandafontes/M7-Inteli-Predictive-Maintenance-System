# -*- coding: utf-8 -*-

import uvicorn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import create_model
from pycaret.classification import load_model, predict_model

# Create input/output pydantic models
class InputData(BaseModel):
    date: str
    precipitation: float
    temp_max: float
    temp_min: float
    wind: float

class OutputData(BaseModel):
    prediction: str

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("api")

# Define predict function
@app.post("/predict", response_model=OutputData)
def predict(data: InputData):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    uvicorn.run(app, port=8000)