import streamlit as st
import os
import joblib
import pandas as pd

st.title("BMI Prediction")

height = st.number_input("ส่วนสูง (cm)", min_value=50, max_value=250)
weight = st.number_input("น้ำหนัก (kg)", min_value=10, max_value=200)
age = st.number_input("อายุ (ปี)", min_value=1, max_value=120)
gender = st.selectbox("เพศ", ["Male", "Female"])


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

model_path = os.path.join(MODEL_DIR, "bmi_model.pkl")
le_path = os.path.join(MODEL_DIR, "label_encoder.pkl")

try:
    model = joblib.load(model_path)
    le = joblib.load(le_path)
except Exception as e:
    st.error(f"ไม่พบไฟล์ bmi_model.pkl หรือ label_encoder.pkl: {e}")
    model = None
    le = None

if st.button("ทำนาย BMI") and model and le:
    try:
        gender_num = 0 if gender == "Male" else 1
        input_data = pd.DataFrame(
            [[weight, height, age, gender_num]],
            columns=["Weight","Height","Age","Gender"]
        )

        pred_encoded = model.predict(input_data)[0]
        pred_label = le.inverse_transform([pred_encoded])[0]

        st.write(f"คาดการณ์ BMI ของคุณ: **{pred_label}**")
    except Exception as e:
        st.error(f"เกิดข้อผิดพลาดในการทำนาย: {e}")
st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("กลับสู่หน้าหลัก"):
    st.switch_page("app.py")