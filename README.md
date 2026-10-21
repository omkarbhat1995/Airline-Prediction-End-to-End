# ✈️ Airline Prediction End-to-End

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red.svg)](https://streamlit.io/)

An end-to-end machine learning pipeline designed to predict airline flight prices (or delays) using historical flight data. This project covers the entire MLOps lifecycle—from data ingestion and complex feature engineering to model training, evaluation, and deployment via an interactive web interface.

## 🚀 Key Features

- **Exploratory Data Analysis (EDA):** Comprehensive analysis of flight trends, airline pricing strategies, and seasonal variations.
- **Advanced Feature Engineering:** Extraction of routing data, cyclic datetime features (departure/arrival hours), and intelligent categorical encoding for airlines and destinations.
- **Machine Learning Modeling:** Built, tuned, and evaluated predictive models using Scikit-Learn to ensure high accuracy and low error rates.
- **Interactive Web Application:** Deployed a user-friendly frontend using **Streamlit**, allowing users to input travel parameters and receive real-time predictive insights.
- **Scalable Architecture:** Codebase structured using Object-Oriented Programming (OOP) principles for easy maintenance and scaling.

## 🛠️ Technologies Used

- **Language:** Python
- **Data Manipulation & Visualization:** Pandas, NumPy, Matplotlib, Seaborn
- **Machine Learning:** Scikit-Learn (Random Forest, Gradient Boosting, etc.)
- **Deployment & API:** Streamlit, FastAPI 
- **Tools:** VS Code, Jupyter Notebook, Docker

## 📂 Repository Structure

```text
Airline-Prediction-End-to-End/
│
├── data/                   # Raw and processed datasets
├── notebooks/              # Jupyter notebooks for EDA and model experimentation
├── src/                    # Source code for data pipelines and ML models
│   ├── data_ingestion.py   
│   ├── data_preprocessing.py
│   └── model_training.py
├── app.py                  # Streamlit web application script
├── model.pkl               # Pickled machine learning model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
