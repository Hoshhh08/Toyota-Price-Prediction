import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the trained Ridge model
with open("trained_ridge_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("scaler.pkl",'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Streamlit UI Setup
st.set_page_config(page_title="Vehicle Price Predictor", layout="centered")

st.title("🚗 Toyota Vehicle Price App")
st.markdown("### ← Enter Vehicle details below to get a price estimate.")

# Sidebar for input features
st.sidebar.header("Vehicle Features")
age = st.sidebar.slider("Vehicle Age (in years)", 6, 80, 50)
km = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=100000, value=10000)
fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "CNG"])
automatic = st.sidebar.selectbox("Automatic Transmission?", ["No", "Yes"])
cc = st.sidebar.number_input("Engine Capacity (cc)", min_value=1300, max_value=2000, value=1500)
doors = st.sidebar.slider("Number of Doors", 2, 5, 4)
gears = st.sidebar.slider("Number of Gears", 3, 6, 5, 4)
weight = st.sidebar.number_input("Weight (kg)", min_value=1000, max_value=1700, value=1200)

# Map "Yes" and "No" to 1 and 0
automatic = 1 if automatic == "Yes" else 0

# One-hot encode the 'fuel_type' feature
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0
fuel_type_cng = 1 if fuel_type == "CNG" else 0

# Prepare input features (this should have 12 features)
input_features = np.array([[age, km, fuel_type_petrol, fuel_type_cng, automatic, cc, doors, gears, weight]])

# Prepare column headers
column_headers = [
    "Car Age (in years)", "Kilometers Driven", "Fuel Type: Petrol",
    "Fuel Type: CNG",
    "Automatic Transmission", "Engine Capacity (cc)",
    "Number of Doors", "Number of Gears", "Weight (kg)"
]

# Prepare input features DataFrame
input_features_df = pd.DataFrame(input_features, columns=column_headers)

# Prediction Button
if st.sidebar.button("Predict Price"):
    try:
        # Make prediction
        predicted_price = model.predict(input_features)[0]
        st.success(f"🚘 Estimated Car Price: **€{predicted_price:,.2f}**")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")