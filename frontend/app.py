import streamlit
import requests
import json
import pandas as pd

df = pd.read_csv("../cleaned_car_data.csv")

        
def run():
    streamlit.title("Car Price Prediction")
    name = streamlit.selectbox("Cars Model", df.name.unique())
    company = streamlit.selectbox("Company Name", df.company.unique())
    year = streamlit.number_input("Year")
    kms_driven = streamlit.number_input("Kilometers driven")
    fuel_type = streamlit.selectbox("Fuel type", df.fuel_type.unique())
    
    data = { 
        'name': name,
        'company': company,
        'year': year,
        'kms_driven': kms_driven,
        'fuel_type': fuel_type,
        }
    
    if streamlit.button("Predict"):
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction =response.text
        streamlit.success(f"The prediction from model: {prediction}")
    
if __name__ == '__main__':
    #by default it will run at 8501 port
    run()