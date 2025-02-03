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

# Custom CSS for background image
background_image_url = "https://live.staticflickr.com/7407/16457676315_d320715422_b.jpg"  # Replace with your image URL

st.markdown(
    f"""
    <style>
    .stApp {{
        background: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚗 Toyota Vehicle Price App")
st.markdown("### ← Enter Vehicle details to get a price estimate.")

# Sidebar for input features
st.sidebar.header("Vehicle Features")
age = st.sidebar.slider("Vehicle Age (in years)", 1, 80, 50)
km = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=500000, value=10000)
fuel_type = st.sidebar.selectbox("Fuel Type", ["Petrol", "CNG"])
automatic = st.sidebar.selectbox("Automatic Transmission?", ["No", "Yes"])
cc = st.sidebar.number_input("Engine Capacity (cc)", min_value=1000, max_value=3000, value=1200)
doors = st.sidebar.slider("Number of Doors", 2, 5, 4)
gears = st.sidebar.slider("Number of Gears", 3, 6, 5, 1)
weight = st.sidebar.number_input("Weight (kg)", min_value=1000, max_value=1700, value=1200)

# Map "Yes" and "No" to 1 and 0
automatic = 1 if automatic == "Yes" else 0

# One-hot encode the 'fuel_type' feature
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0
fuel_type_cng = 1 if fuel_type == "CNG" else 0

# Prepare input features in the correct order
input_features = np.array([[age, km, automatic, cc, doors, gears, weight, fuel_type_cng, fuel_type_petrol]])

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
        # Scale the input using the saved scaler
        scaled_input = scaler.transform(input_features)

        # Make prediction
        predicted_price = model.predict(scaled_input)[0]

        # Ensure non-negative price
        predicted_price = max(0, predicted_price)

        st.success(f"🚘 Estimated Car Price: **€{predicted_price:,.2f}**")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
