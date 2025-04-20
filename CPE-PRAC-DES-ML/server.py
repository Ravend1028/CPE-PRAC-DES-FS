from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Load the trained model
model = joblib.load('model.joblib')

# Define the expected input features
FEATURE_COLUMNS = [
    'Height (cm)', 'Weight (kg)', 'BMI', 'Systolic BP', 'Diastolic BP',
    'Pulse Rate', 'Respiratory Rate', 'Body Temperature (°C)', 'Blood Oxygen Level (%)'
]

# Create FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or set to ["http://localhost:5173"] for more security
    allow_credentials=True,
    allow_methods=["*"],  # Allows POST, GET, OPTIONS, etc.
    allow_headers=["*"],  # Allows all headers including Content-Type
)

# Request body schema using Pydantic
class ModelInput(BaseModel):
    features: list[float]

@app.get('/')
def read_root():
    return { 'message': 'Hello World!' }

@app.post("/predict")
def predict(input_data: ModelInput):
    if len(input_data.features) != len(FEATURE_COLUMNS):
        return {"error": f"Expected {len(FEATURE_COLUMNS)} features, but got {len(input_data.features)}."}

    # Convert to DataFrame just like in Colab
    input_df = pd.DataFrame([input_data.features], columns=FEATURE_COLUMNS)

    # Make prediction
    prediction = model.predict(input_df)

    # Define output labels
    OUTPUT_COLUMNS = [
        'Underweight', 'Overweight', 'Obesity', 'Hypertension', 'Hypotension',
        'Hypoxia', 'Fever', 'Hypothermia', 'Bradycardia', 'Tachycardia', 'Respiratory Distress'
    ]
    
    # Return prediction as a dict
    prediction_df = pd.DataFrame(prediction, columns=OUTPUT_COLUMNS)
    return prediction_df.iloc[0].to_dict()