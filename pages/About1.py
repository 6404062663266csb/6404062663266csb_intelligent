import streamlit as st

st.set_page_config(
    page_title="อธิบาย Machine Learning (BMI)",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.main {
    background-color: #0f172a;
}
h1, h2 {
    color: #e5e7eb;
}
p {
    color: #cbd5f5;
    font-size: 17px;
    line-height: 1.8;
}
.box {
    background-color: #020617;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 0 30px rgba(0,255,180,0.08);
}
.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='center'>อธิบายการพัฒนาโมเดล Machine Learning (BMI)</h1>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class="box">
<p>
พัฒนาโมเดล Machine Learning 
สำหรับคำนวณและจำแนกภาวะร่างกายของผู้ใช้งานจากค่า BMI 
</p>

<p>
Dataset เป็น Dataset ประเภท Structured Data ใช้ chat gpt สร้างขึ้น
โดยอ้างอิงหลักการคำนวณ BMI ตามมาตรฐานสากล ข้อมูลถูกจัดเก็บในรูปแบบไฟล์ CSV 
ประกอบด้วยข้อมูลน้ำหนัก ส่วนสูง อายุ และเพศ รวมถึงกลุ่มภาวะร่างกาย
</p>

<p>
ก่อนนำข้อมูลไปพัฒนาโมเดล ได้มีการเตรียมข้อมูลเบื้องต้น ได้แก่ 
การตรวจสอบความถูกต้องของข้อมูล และการแปลงข้อมูลเพศจากข้อความให้เป็นข้อมูลตัวเลข 
เพื่อให้สามารถนำไปใช้กับ Machine Learning ได้
</p>

<p>
ระบบจะรับข้อมูลจากผู้ใช้งาน ได้แก่ น้ำหนัก ส่วนสูง อายุ และเพศ 
จากนั้นคำนวณค่า BMI และจำแนกผลลัพธ์ออกเป็นกลุ่มภาวะร่างกาย 
เช่น ผอม ปกติ น้ำหนักเกิน และอ้วน
</p>

            
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("กลับสู่หน้าหลัก"):
    st.switch_page("app.py")