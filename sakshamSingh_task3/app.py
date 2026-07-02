import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("model/car_price_model.pkl")
columns = joblib.load("model/model_columns.pkl")

st.title("🚗 Car Price Prediction")

present_price = st.number_input(
    "Present Price (Lakhs)",
    min_value=0.0
)

driven_kms = st.number_input(
    "Driven Kilometers",
    min_value=0
)

owner = st.selectbox(
    "Number of Previous Owners",
    [0,1,2,3]
)

car_age = st.slider(
    "Car Age",
    0,
    20,
    5
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol", "Diesel", "CNG"]
)

selling_type = st.selectbox(
    "Selling Type",
    ["Dealer", "Individual"]
)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

if st.button("Predict Price"):

    input_data = {
        "Present_Price": present_price,
        "Driven_kms": driven_kms,
        "Owner": owner,
        "Car_Age": car_age,
        "Fuel_Type_Diesel": 0,
        "Fuel_Type_Petrol": 0,
        "Selling_type_Individual": 0,
        "Transmission_Manual": 0
    }

    if fuel == "Diesel":
        input_data["Fuel_Type_Diesel"] = 1

    elif fuel == "Petrol":
        input_data["Fuel_Type_Petrol"] = 1

    if selling_type == "Individual":
        input_data["Selling_type_Individual"] = 1

    if transmission == "Manual":
        input_data["Transmission_Manual"] = 1

    input_df = pd.DataFrame(
        [input_data]
    )

    input_df = input_df.reindex(
        columns=columns,
        fill_value=0
    )

    prediction = model.predict(input_df)

    st.success(
        f"Estimated Car Price: ₹ {prediction[0]:.2f} Lakhs"
    )