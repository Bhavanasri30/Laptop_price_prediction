import pandas as pd

brand = st.number_input("Brand (Encoded Value)", min_value=0, step=1)
processor_speed = st.number_input("Processor Speed (GHz)", min_value=1.0, max_value=6.0, step=0.1)
ram = st.number_input("RAM Size (GB)", min_value=2, max_value=64, step=2)
storage = st.number_input("Storage Capacity (GB)", min_value=128, max_value=2000, step=128)
screen_size = st.number_input("Screen Size (inches)", min_value=10.0, max_value=20.0, step=0.1)
weight = st.number_input("Weight (kg)", min_value=0.5, max_value=5.0, step=0.1)

if st.button("Predict Price"):

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

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)

    st.success(f"💰 Predicted Laptop Price: ₹ {round(prediction[0], 2)}")