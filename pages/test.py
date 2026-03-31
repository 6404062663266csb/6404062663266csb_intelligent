import streamlit as st
import joblib
import pandas as pd

# โหลด model
model = joblib.load("models/nn_model.pkl")
le = joblib.load("models/label_encoder.pkl")

st.title("🧠 Student Pass/Fail Prediction (Neural Network)")

# input
study = st.number_input("Hours Studied", 0, 12, 4)
sleep = st.number_input("Sleep Hours", 0, 12, 6)
attendance = st.number_input("Attendance (%)", 0, 100, 70)
previous = st.number_input("Previous Grade", 0, 100, 60)
internet = st.number_input("Internet Usage (hours/day)", 0, 12, 3)

# predict
if st.button("Predict"):
    data = pd.DataFrame([[study, sleep, attendance, previous, internet]],
        columns=["Hours_Studied","Sleep_Hours","Attendance","Previous_Grade","Internet_Usage"]
    )

    pred = model.predict(data)
    result = le.inverse_transform(pred)

    st.success(f"Result: {result[0]}")