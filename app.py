# ===============================
# Laptop Price Prediction App
# ===============================

import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------
# Load Model and Scaler
# -------------------------------

model = pickle.load(open("linear_regression_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -------------------------------
# Page Setup
# -------------------------------

st.set_page_config(page_title="Laptop Price Predictor")
st.title("💻 Laptop Price Prediction")
st.write("Enter laptop specifications below:")

st.markdown("---")

# -------------------------------
# User Inputs
# -------------------------------

brand = st.number_input("Brand (Encoded Value)", min_value=0, step=1)
processor_speed = st.number_input("Processor Speed (GHz)", min_value=1.0, max_value=6.0, step=0.1)
ram = st.number_input("RAM Size (GB)", min_value=2, max_value=64, step=2)
storage = st.number_input("Storage Capacity (GB)", min_value=128, max_value=2000, step=128)
screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)

# -------------------------------
# Prediction
# -------------------------------

if st.button("Predict Price"):

    # IMPORTANT: Column names must match training dataset
    input_df = pd.DataFrame(
        [[brand, processor_speed, ram, storage, screen_size, weight]],
        columns=[
            "0Brand",
            "Processor_Speed",
            "RAM_Size",
            "Storage_Capacity",
            "Screen_Size",
            "Weight"
        ]
    )

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction = model.predict(input_scaled)

    st.success(f"💰 Predicted Laptop Price: ₹ {round(prediction[0], 2)}")
