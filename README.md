# 🩺 Diabetes Prediction System

An AI-powered multi-page web application that predicts diabetes risk and provides personalized health recommendations. Built with Python, Scikit-learn, and Streamlit.

## 🌟 Live Demo

Run locally using the installation steps below.

## 📌 About The Project

Diabetes is one of the most common chronic diseases worldwide. Early detection can save lives. This application uses Machine Learning to predict whether a person is at risk of diabetes based on their medical parameters — all in just a few seconds!

## 🗂️ Pages

- 🏠 **Home** — Welcome page with project overview, features and how to use guide
- 🔍 **Prediction** — Enter your details and get instant diabetes risk prediction
- ℹ️ **About** — Introduction to the project and how the website works
- 📞 **Contact** — Get in touch and FAQ section

## ✨ Key Features

- 🔍 **Diabetes Risk Prediction** — Instant prediction with probability score
- 📏 **BMI Calculator** — Auto-calculates BMI from height and weight
- 📋 **Patient Report** — Detailed personalized report with all parameters
- 💊 **Health Tips** — Diet, exercise and medical tips based on risk level
- ❓ **FAQ Section** — Answers to commonly asked questions

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Scikit-learn | Machine Learning model |
| Streamlit | Multi-page web application |

## 📊 Dataset

- **Name:** Pima Indians Diabetes Dataset
- **Source:** UCI Machine Learning Repository
- **Size:** 768 patient records, 8 medical features
- **Target:** Diabetes Positive or Negative

## 🤖 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Logistic Regression |
| Accuracy | ~75% |
| Train/Test Split | 80% / 20% |

## 📁 Project Structure

- **Home.py** → Main home page
- **pages/1_Prediction.py** → Diabetes prediction page
- **pages/2_About.py** → About the project
- **pages/3_Contact.py** → Contact and FAQ page
- **requirements.txt** → Required libraries
- **README.md** → Project documentation

## ⚙️ Installation & Setup

**1. Clone the repository:**
```bash
git clone https://github.com/tanishkasaraswat23/Diabetes-prediction-system-.git
```

**2. Install required libraries:**
```bash
pip install -r requirements.txt
```

**3. Run the application:**
```bash
streamlit run Home.py
```

## 🚀 How To Use

1. Open the application in your browser
2. Go to **Prediction** page from the sidebar
3. Enter your personal details (name, age, gender)
4. Enter height and weight → BMI auto-calculates
5. Enter medical details (glucose, blood pressure, etc.)
6. Click **"Predict Diabetes Risk"**
7. View your personalized report with health tips!

## 🎓 Learning Outcomes

Through this project, I learned:
- End-to-end Machine Learning pipeline development
- Data preprocessing and feature scaling
- Logistic Regression for classification problems
- Building multi-page interactive web apps with Streamlit
- UI/UX design using HTML and CSS in Streamlit
- Version control with Git and GitHub

## 👩‍💻 Author

**Tanishka Saraswat**
B.Tech AI & ML Student
GitHub: [@tanishkasaraswat23](https://github.com/tanishkasaraswat23)

## ⚠️ Disclaimer

This application is for **educational purposes only**.
It is not a substitute for professional medical advice.
Always consult a qualified doctor for medical diagnosis.