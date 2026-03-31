import streamlit as st

st.set_page_config(
    page_title="Intelligent Project",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #ffffff;
}

h1 {
    text-align: center;
    margin-top: 40px;
}

.subtitle {
    text-align: center;
    color: #475569;
    margin-bottom: 50px;
}

/* container กลาง */
.center-wrap {
    max-width: 1100px;
    margin: auto;
}

/* card */
.card {
    background: #020617;
    border-radius: 20px;
    padding: 25px;
    height: 220px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

/* title */
.card-title {
    font-size: 20px;
    font-weight: bold;
    color: #22c55e;
}

/* description */
.card-desc {
    color: #e5e7eb;
    font-size: 14px;
    margin-top: 10px;
}

/* button wrapper */
.btn-wrap {
    text-align: center;
    margin-top: 12px;
}

/* footer */
.footer {
    margin-top: 70px;
    text-align: center;
    color: #64748b;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>Intelligent System Project</h1>", unsafe_allow_html=True)


st.markdown('<div class="center-wrap">', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">BMI</div>
            <div class="card-desc">
                คำนวณค่า BMI และจำแนกภาวะร่างกาย (Machine Learning)
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="btn-wrap">', unsafe_allow_html=True)
    if st.button("ดูรายละเอียด", key="bmi"):
        st.switch_page("pages/BMI.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">AI Prediction</div>
            <div class="card-desc">
                ระบบทำนายผลด้วยโมเดล Machine Learning
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="btn-wrap">', unsafe_allow_html=True)
    if st.button("ดูรายละเอียด", key="ai"):
        st.switch_page("pages/About1.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">student performance</div>
            <div class="card-desc">
                pass / fail
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="btn-wrap">', unsafe_allow_html=True)
    if st.button("ดูรายละเอียด", key="about"):
        st.switch_page("pages/test.py")
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div>
            <div class="card-title">Natural Machineleaning</div>
            <div class="card-desc">
                หลักการทำงาน โมเดล และขั้นตอนพัฒนา ของหน้า student performance
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="btn-wrap">', unsafe_allow_html=True)
    if st.button("ดูรายละเอียด", key="author"):
        st.switch_page("pages/NN_explain.py")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer">
จัดทำโดย 6404062663266 ศุภกฤต แก้วผลึก<br>
            วิชา Intelligent System | ปีการศึกษา 2/2568<br>
            dataset by chat gpt
</div>
""", unsafe_allow_html=True)