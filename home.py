import streamlit as st

st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""
<style>
.feature-box {
    background-color: #F0F8FF;
    padding: 20px;
    border-radius: 10px;
    border-left: 5px solid #2E86AB;
    margin-bottom: 15px;
    height: 100px;
}
.stats-box {
    background-color: #E8F8F0;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    border: 2px solid #2ECC71;
}
.warning-box {
    background-color: #FFF9E6;
    padding: 15px;
    border-radius: 10px;
    border-left: 5px solid #F39C12;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("🩺 AI-Powered Early Diabetes Risk Detection")

st.markdown("""
<div style="background: linear-gradient(135deg, #2E86AB, #1a5276); padding: 25px; border-radius: 15px; text-align: center; margin: 20px 0px;">
<h3 style="color:white; margin:0;">💬 "Take care of your body.</h3>
<h3 style="color:#AED6F1; margin:0;">It's the only place you have to live."</h3>
<p style="color:#D5E8D4; margin-top:10px;">— Early detection of diabetes can save lives. Check your risk today.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

col_img1, col_img2, col_img3 = st.columns(3)
with col_img1:
    st.markdown("""
    <div style="text-align:center; font-size:60px;">🏥</div>
    <p style="text-align:center; font-weight:bold;">Medical AI</p>
    """, unsafe_allow_html=True)
with col_img2:
    st.markdown("""
    <div style="text-align:center; font-size:60px;">🔬</div>
    <p style="text-align:center; font-weight:bold;">Data Science</p>
    """, unsafe_allow_html=True)
with col_img3:
    st.markdown("""
    <div style="text-align:center; font-size:60px;">💡</div>
    <p style="text-align:center; font-weight:bold;">Smart Insights</p>
    """, unsafe_allow_html=True)

st.write("---")

st.subheader("🌟 Welcome!")
st.write("""
Diabetes is one of the most common chronic diseases worldwide, affecting **millions of people** every year.
Early detection can make a significant difference in managing and preventing serious complications.

This **AI-powered application** uses Machine Learning to predict your diabetes risk instantly 
based on your medical parameters — helping you take proactive steps towards better health. 💪
""")

st.write("---")
st.subheader("✨ Key Features")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="feature-box">
    <b>🔍 Diabetes Risk Prediction</b><br>
    Instant prediction with probability score using Logistic Regression
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-box">
    <b>📏 BMI Calculator</b><br>
    Auto-calculates BMI from your height and weight instantly
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <b>📋 Patient Report</b><br>
    Detailed personalized report with all your medical parameters
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="feature-box">
    <b>💊 Health Tips</b><br>
    Personalized diet, exercise and medical recommendations
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.subheader("🚀 How To Use")

col6, col7, col8, col9 = st.columns(4)
with col6:
    st.markdown("""
    <div style="text-align:center;">
    <div style="font-size:40px;">1️⃣</div>
    <p><b>Click Prediction</b><br>in the sidebar</p>
    </div>
    """, unsafe_allow_html=True)
with col7:
    st.markdown("""
    <div style="text-align:center;">
    <div style="font-size:40px;">2️⃣</div>
    <p><b>Enter Details</b><br>personal & medical</p>
    </div>
    """, unsafe_allow_html=True)
with col8:
    st.markdown("""
    <div style="text-align:center;">
    <div style="font-size:40px;">3️⃣</div>
    <p><b>Click Predict</b><br>get instant result</p>
    </div>
    """, unsafe_allow_html=True)
with col9:
    st.markdown("""
    <div style="text-align:center;">
    <div style="font-size:40px;">4️⃣</div>
    <p><b>View Report</b><br>with health tips</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")
st.markdown("""
<div class="warning-box">
⚠️ <b>Disclaimer:</b> This application is for <b>educational purposes only</b>.<br>
Always consult a qualified doctor for medical advice.
</div>
""", unsafe_allow_html=True)