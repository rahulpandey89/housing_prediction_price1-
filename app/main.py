import sys
import os

# add parent folder (housing_prediction) to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fastapi import FastAPI, UploadFile, File
from src.preprocess import preprocess_file # tumhara existing function
from src.predict import predict 
import pandas as pd

app = FastAPI()
@app.get("/")   # root endpoint
def read_root():
    return {"message": "Server is running!"}

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    # 1️⃣ CSV read
    df = pd.read_csv(file.file)
    df_processed = preprocess_file(df)
    
    predictions = predict(df_processed)
    df["predicted_price"] = predictions
    print(df[["predicted_price"]].head())
    return df.to_html()