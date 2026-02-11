import streamlit as st
import numpy as np
import pickle

# Load saved model
with open("linear_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load saved scaler
with open("scaler.pkl", "rb") as file:
    scaler = pickle.load(file)

st.set_page_config(page_title="Laptop Price Predictor")

st.title("💻 Laptop Price Prediction App")
st.write("Enter laptop specifications to predict the price.")

st.markdown("---")

# Example input fields (Modify according to your dataset columns)

ram = st.number_input("RAM (GB)", min_value=2, max_value=64, step=2)
storage = st.number_input("Storage (GB)", min_value=128, max_value=2000, step=128)
screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)

# If you encoded processor as numeric:
processor = st.number_input("Processor Type (Encoded Value)", min_value=0, step=1)

# Predict Button
if st.button("Predict Price"):

    # Create input array (ORDER must match training features)
    input_data = np.array([[ram, storage, screen_size, weight, processor]])

    # Scale input
    input_scaled = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(input_scaled)

    st.success(f"💰 Predicted Laptop Price: ₹ {round(prediction[0], 2)}")
