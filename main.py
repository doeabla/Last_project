from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from typing import Union
 
# encoder = joblib.load("labelencoder.joblib")
pipeline = joblib.load("logisticregressionpipeline.joblib")
 
# create an instance
app = FastAPI()
 
#to read on the screen 
@app.get("/")
def sephome():
    return("New Sepsis Prediction app")

# create a class to define the dataypes 
class InputData(BaseModel):
    Plasma_glucose: int
    Blood_work1: int
    Blood_Pressure: int
    Blood_work2: int
    Blood_work3: int
    BMI: float
    Blood_work4: float
    Age: int
    Insurance: int
    #Sepsis: object
 
@app.get("/") 
def home():
    return ("SEPSIS PREDICTION APP API")

@app.get("/")
def appinfo():
    return ("This is a API for the Sepsis Prediction App")


# initialize the prediction end point
class PredictionResult(BaseModel):
    prediction: str  # Assuming it's a binary classification
 
# create a dataframe for pipeline to use for prediction  
@app.post("/predict", response_model=PredictionResult)
def predict(InputData: InputData):
    
    # model dumb for single line of code
    try:
        df = pd.DataFrame([InputData.model_dump() ])
 
        preprocessed_data = pipeline.predict(df)
        #encoded_target = encoder.transform(np.array([data.Sepsis]))

        # Set the prediction output
        # Assuming preprocessed_data[0] is the predicted probability, you might want to threshold it
        prediction_value = "Positive" if preprocessed_data[0] >= 0.5 else "Negative"
 
        return PredictionResult(prediction=prediction_value)
 
    except ValueError as ve:
        return PredictionResult(prediction=None, error=f"ValueError: {str(ve)}")
 
    except Exception as e:
        return PredictionResult(prediction=None, error=f"Internal Server Error: {str(e)}")