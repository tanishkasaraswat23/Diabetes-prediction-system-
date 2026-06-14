import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Diabetes Prediction System", page_icon="🩺")

st.title("🩺 Diabetes Prediction System")
st.write("Fill in your details below to check your diabetes risk.")

@st.cache_resource
def train_model():
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
    columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
               "Insulin", "BMI", "DiabetesPedigree", "Age", "Outcome"]
    df = pd.read_csv(url, names=columns)
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train_scaled, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test_scaled))
    return model, scaler, accuracy

with st.spinner("Loading Model... Please wait!"):
    model, scaler, accuracy = train_model()

st.info(f"Model Accuracy: {accuracy*100:.2f}%")
st.write("---")

st.subheader("👤 Personal Information")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name", placeholder="Enter your name")
with col2:
    age = st.number_input("Age", min_value=1, max_value=120, value=25)
gender = st.selectbox("Gender", ["Female", "Male", "Other"])

st.write("---")
st.subheader("📏 BMI Calculator")
st.write("Enter height and weight to calculate BMI automatically!")
col3, col4 = st.columns(2)
with col3:
    height = st.number_input("Height (cm)", min_value=100, max_value=250, value=165)
with col4:
    weight = st.number_input("Weight (kg)", min_value=20, max_value=200, value=60)

bmi = round(weight / ((height / 100) ** 2), 2)
if bmi < 18.5:
    bmi_category = "Underweight 🔵"
elif bmi < 25:
    bmi_category = "Normal Weight 🟢"
elif bmi < 30:
    bmi_category = "Overweight 🟡"
else:
    bmi_category = "Obese 🔴"
st.success(f"Your BMI: **{bmi}** → {bmi_category}")

st.write("---")
st.subheader("🏥 Medical Details")
col5, col6 = st.columns(2)
with col5:
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
with col6:
    insulin = st.number_input("Insulin Level (IU/mL)", min_value=0, max_value=900, value=79)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)

st.write("---")
predict_button = st.button("🔍 Predict Diabetes Risk")

if predict_button:
    if name == "":
        st.warning("⚠️ Please enter your name first!")
    else:
        input_df = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigree": [diabetes_pedigree],
            "Age": [age]
        })

        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        probability = model.predict_proba(input_scaled)

        st.write("---")
        st.subheader(f"📋 Report for {name}")

        col7, col8 = st.columns(2)
        with col7:
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age} years")
            st.write(f"**Gender:** {gender}")
            st.write(f"**BMI:** {bmi} ({bmi_category})")
        with col8:
            st.write(f"**Glucose:** {glucose} mg/dL")
            st.write(f"**Blood Pressure:** {blood_pressure} mm Hg")
            st.write(f"**Insulin:** {insulin} IU/mL")
            st.write(f"**Pregnancies:** {pregnancies}")

        st.write("---")
        if prediction[0] == 1:
            risk = probability[0][1] * 100
            st.error(f"⚠️ High Risk of Diabetes!")
            st.error(f"Probability: {risk:.2f}%")

            st.subheader("💊 Health Tips for High Risk:")
            st.write("**🥗 Diet Tips:**")
            st.write("• Avoid sugary drinks and sweets")
            st.write("• Eat more vegetables and whole grains")
            st.write("• Reduce white rice and white bread")
            st.write("• Eat small meals every 3-4 hours")
            st.write("• Drink 8-10 glasses of water daily")

            st.write("**🏃 Exercise Tips:**")
            st.write("• Walk for 30 minutes daily")
            st.write("• Do light yoga or stretching")
            st.write("• Avoid sitting for long hours")
            st.write("• Exercise at least 5 days a week")

            st.write("**👨‍⚕️ Medical Tips:**")
            st.write("• Consult a doctor immediately")
            st.write("• Monitor glucose levels daily")
            st.write("• Get HbA1c test done")
            st.write("• Check blood pressure regularly")

        else:
            risk = probability[0][0] * 100
            st.success(f"✅ Low Risk of Diabetes!")
            st.success(f"Probability: {risk:.2f}%")

            st.subheader("💚 Tips to Stay Healthy:")
            st.write("**🥗 Diet Tips:**")
            st.write("• Maintain a balanced diet")
            st.write("• Include fruits and vegetables daily")
            st.write("• Limit junk food and processed food")
            st.write("• Stay hydrated - drink plenty of water")

            st.write("**🏃 Exercise Tips:**")
            st.write("• Exercise at least 3-4 times a week")
            st.write("• Include both cardio and strength training")
            st.write("• Stay active throughout the day")

            st.write("**👨‍⚕️ Preventive Tips:**")
            st.write("• Get annual health checkups")
            st.write("• Monitor your weight regularly")
            st.write("• Maintain healthy BMI")
            st.write("• Avoid smoking and alcohol")

st.write("---")
st.write("⚠️ This is for educational purposes only. Consult a doctor for medical advice.")