# 🩺 Diabetes Prediction System

A Machine Learning web application that predicts diabetes risk and provides personalized health recommendations. Built with Python, Scikit-learn, and Streamlit.

## 🌟 Live Demo

Run locally using the installation steps below.

## 📌 About The Project

Diabetes is one of the most common chronic diseases worldwide. Early detection can save lives. This application uses Machine Learning to predict whether a person is at risk of diabetes based on their medical parameters — all in just a few seconds!

## ✨ Key Features

- 🔍 **Diabetes Risk Prediction** — Instant prediction with probability score
- 📏 **BMI Calculator** — Auto-calculates BMI from height and weight
- 📋 **Patient Report** — Detailed personalized report with all parameters
- 💊 **Health Tips** — Diet, exercise and medical tips based on risk level
- ⚡ **Real-time Results** — Instant predictions with no delay

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Scikit-learn | Machine Learning model |
| Streamlit | Interactive web application |

## 📊 Dataset

- **Name:** Pima Indians Diabetes Dataset
- **Source:** UCI Machine Learning Repository
- **Size:** 768 patient records, 8 medical features
- **Target:** Diabetes Positive or Negative

### Features Used:

| Feature | Description |
|---------|-------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mm Hg) |
| Skin Thickness | Triceps skin fold thickness (mm) |
| Insulin | 2-Hour serum insulin (IU/mL) |
| BMI | Body Mass Index |
| Diabetes Pedigree | Diabetes pedigree function |
| Age | Age in years |

## 🤖 Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Logistic Regression |
| Accuracy | ~75% |
| Train/Test Split | 80% / 20% |

## 📁 Project Structure

- **app.py** → Main Streamlit application
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
streamlit run app.py
```

## 🚀 How To Use

1. Enter your **personal details** (name, age, gender)
2. Enter your **height and weight** → BMI auto-calculates
3. Enter your **medical details** (glucose, blood pressure, etc.)
4. Click **"Predict Diabetes Risk"** button
5. View your **personalized report** with health tips!

## 📈 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Below 18.5 | Underweight 🔵 |
| 18.5 - 24.9 | Normal Weight 🟢 |
| 25.0 - 29.9 | Overweight 🟡 |
| 30.0 and above | Obese 🔴 |

## 🎓 Learning Outcomes

Through this project, I learned:
- End-to-end Machine Learning pipeline development
- Data preprocessing and feature scaling
- Logistic Regression for classification problems
- Building interactive web apps with Streamlit
- Version control with Git and GitHub

## 👩‍💻 Author

**Tanishka Saraswat**
B.Tech AI & ML @ Aravali College of Engineering & Management
GitHub: [@tanishkasaraswat23](https://github.com/tanishkasaraswat23)

## ⚠️ Disclaimer

This application is for **educational purposes only**.
It is not a substitute for professional medical advice.
Always consult a qualified doctor for medical diagnosis.