# Import Needed Libraries
import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel

# FastAPI libray
from fastapi import FastAPI

# Initiate app instance
app = FastAPI(title='Car Price Prediction', version='1.0',
              description='Linear Regression model is used for prediction')

# Initialize model artifacte files. This will be loaded at the start of FastAPI model server.
model = joblib.load("LinearRegressionModel.joblib")

# This struture will be used for Json validation.
# With just that Python type declaration, FastAPI will perform below operations on the request data
## 1) Read the body of the request as JSON.
## 2) Convert the corresponding types (if needed).
## 3) Validate the data.If the data is invalid, it will return a nice and clear error, 
##    indicating exactly where and what was the incorrect data.
class Data(BaseModel):
    name: str
    company: str
    year: int
    kms_driven: float
    fuel_type: str  
    

# Api root or home endpoint
@app.get('/')
@app.get('/home')
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {'message': 'System is healthy'}

# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict(data: Data):

    result = model.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([data.name,data.company,data.year,data.kms_driven,data.fuel_type]).reshape(1,5)))[0]
    return result

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)