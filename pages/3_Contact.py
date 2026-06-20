import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞")

st.title("📞 Contact Us")
st.write("---")

st.subheader("💬 Have Questions or Feedback?")
st.write("""
We would love to hear from you! Whether you have questions about the application, 
feedback about the predictions, or just want to connect — feel free to reach out!
""")

st.write("---")

st.subheader("📬 Get In Touch")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#F0F8FF; padding:25px; border-radius:10px; border-left:5px solid #2E86AB; text-align:center;">
    <div style="font-size:50px;">📞</div>
    <h4>Call Us</h4>
    <p style="font-size:18px;"><b>+91 98765 43210</b></p>
    <p style="color:gray;">Mon - Sat | 9 AM - 6 PM</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color:#F0F8FF; padding:25px; border-radius:10px; border-left:5px solid #2E86AB; text-align:center;">
    <div style="font-size:50px;">📧</div>
    <h4>Email Us</h4>
    <p style="font-size:18px;"><b>diabetescare@gmail.com</b></p>
    <p style="color:gray;">We reply within 24 hours</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.subheader("❓ Frequently Asked Questions")

with st.expander("Is this app accurate for medical diagnosis?"):
    st.write("""
    No. This application is built for educational purposes only. 
    The model has an accuracy of approximately 75%, which means it can make mistakes. 
    Always consult a qualified doctor for medical diagnosis.
    """)

with st.expander("What data does this app use?"):
    st.write("""
    The model is trained on the Pima Indians Diabetes Dataset which contains 
    768 patient records. Your input data is NOT stored anywhere — 
    it is only used for the prediction and is discarded after the session ends.
    """)

with st.expander("How can I improve my prediction accuracy?"):
    st.write("""
    Make sure to enter accurate medical values. Consult your doctor to get 
    the correct values for glucose level, blood pressure, insulin, and other parameters 
    before using this application.
    """)

with st.expander("Can I use this for someone else?"):
    st.write("""
    Yes! You can enter details for a family member or friend. 
    Just make sure to enter their correct medical parameters for accurate results.
    """)

st.write("---")
st.markdown("""
<p style='text-align:center; color:gray;'>
⚠️ This application is for educational purposes only.<br>
Always consult a qualified doctor for medical advice.
</p>
""", unsafe_allow_html=True)