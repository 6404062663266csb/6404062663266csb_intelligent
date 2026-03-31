import streamlit as st

st.title("Neural Network Explanation")

st.markdown("""
## Neural Network คืออะไร?
Neural Network เป็นโมเดล Machine Learning ที่เลียนแบบการทำงานของสมองมนุษย์  
โดยมีโครงสร้างเป็น Layer ได้แก่:
- Input Layer
- Hidden Layer
- Output Layer

แต่ละ node จะเชื่อมกันด้วย weight และ bias
""")

st.markdown("""
## โครงสร้างของโมเดลที่ใช้ในโปรเจคนี้
- Input: Weight, Height, Age, Gender
- Hidden Layer: 2 ชั้น
- Activation Function: ReLU
- Output: Class BMI (Underweight, Normal, Overweight, Obese)
""")

st.markdown("""
##  ขั้นตอนการทำงาน
1. รับข้อมูลจากผู้ใช้
2. ส่งข้อมูลเข้า Neural Network
3. คำนวณผ่าน weight + activation
4. ทำนายผลลัพธ์
""")

st.markdown("""
## เปรียบเทียบกับ Machine Learning (Ensemble)

| หัวข้อ | Machine Learning | Neural Network |
|------|----------------|----------------|
| ความซับซ้อน | ต่ำ | สูง |
| ความแม่นยำ | ปานกลาง | สูง |
| การเรียนรู้ | Feature-based | Deep learning |
| การใช้งาน | ง่าย | ซับซ้อน |
""")

if st.button("กลับหน้าหลัก"):
    st.switch_page("app.py")