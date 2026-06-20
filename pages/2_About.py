import streamlit as st

st.set_page_config(page_title="About", page_icon="ℹ️")

st.markdown("""
    <style>
    .about-title {
        text-align: center;
        font-size: 52px;
        font-weight: bold;
        color: #2E86AB;
    }
    .intro-box {
        background: linear-gradient(135deg, #2E86AB, #1a5276);
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0px;
    }
    .step-box {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2E86AB;
        margin-bottom: 15px;
    }
    .info-box {
        background-color: #E8F8F0;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #2ECC71;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)
st.title("ℹ️ About Us")
st.write("---")

st.markdown("""
<div class="intro-box">
<h3 style="color:white; margin:0;">Welcome to Diabetes Prediction System</h3>
<p style="color:#AED6F1; margin-top:10px; font-size:16px;">
An AI-powered platform dedicated to helping people detect 
diabetes risk early and take control of their health.
</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

st.subheader("📌 Who We Are")
st.write("""
We are a team of AI & Machine Learning enthusiasts who believe that 
**technology can save lives**. This platform was built with a simple mission — 
to make early diabetes detection accessible to everyone, anywhere, anytime.

Diabetes affects millions of people worldwide, and most cases go undetected 
until it's too late. Our goal is to give people a simple, fast, and 
intelligent tool to understand their health better.
""")

st.write("---")

st.subheader("🎯 Our Mission")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div style="text-align:center; padding:20px; background:#F0F8FF; border-radius:10px;">
    <div style="font-size:45px;">🎯</div>
    <h4>Early Detection</h4>
    <p>Help users identify diabetes risk before it becomes serious</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div style="text-align:center; padding:20px; background:#F0F8FF; border-radius:10px;">
    <div style="font-size:45px;">💡</div>
    <h4>Awareness</h4>
    <p>Educate users about diabetes symptoms and prevention</p>
    </div>
    """, unsafe_allow_html=True)
with col3:
    st.markdown("""
    <div style="text-align:center; padding:20px; background:#F0F8FF; border-radius:10px;">
    <div style="font-size:45px;">❤️</div>
    <h4>Better Health</h4>
    <p>Provide personalized health tips for a healthier lifestyle</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.subheader("🌐 How Our Website Works")

st.markdown("""
<div class="step-box">
<b>Step 1: 🏠 Home Page</b><br>
Get an overview of what our platform offers. Learn about diabetes, 
our features, and how the application can help you stay healthy.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
<b>Step 2: 🔍 Prediction Page</b><br>
Enter your personal details like name, age, and gender. Then enter 
your medical parameters including glucose level, blood pressure, 
insulin, and more. Our AI model will instantly analyze your data.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
<b>Step 3: 📋 Get Your Report</b><br>
After clicking Predict, you will receive a detailed personal report 
showing your diabetes risk level with a probability score. Your BMI 
is automatically calculated from your height and weight.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
<b>Step 4: 💊 Health Tips</b><br>
Based on your prediction result, you will receive personalized diet tips, 
exercise recommendations, and medical advice tailored specifically to 
your risk level — high risk or low risk.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="step-box">
<b>Step 5: 📞 Contact Us</b><br>
Have questions or feedback? Visit our Contact page to send us a message 
or check our FAQ section for commonly asked questions.
</div>
""", unsafe_allow_html=True)

st.write("---")

st.subheader("💊 What is Diabetes?")
st.markdown("""
<div class="info-box">
Diabetes is a chronic disease that occurs when the body cannot properly 
process blood sugar (glucose). There are two main types:

<br><br>

🔴 <b>Type 1 Diabetes</b> — The body does not produce insulin at all. 
Usually diagnosed in children and young adults.

<br><br>

🟡 <b>Type 2 Diabetes</b> — The body does not use insulin properly. 
This is the most common type and is often linked to lifestyle factors 
like diet, exercise, and weight.

<br><br>

⚠️ <b>Early detection and lifestyle changes</b> can significantly reduce 
the risk of complications like heart disease, kidney failure, and vision loss.
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<p style='text-align:center; color:gray;'>
⚠️ This application is for educational purposes only.<br>
Always consult a qualified doctor for medical advice.
</p>
""", unsafe_allow_html=True)