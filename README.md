# 🍷 Wine Quality Prediction (End-to-End ML Project)

## 📌 Overview

This project predicts the quality of wine based on physicochemical properties using Machine Learning.

It covers the complete ML lifecycle — from data analysis to model deployment using a Flask API.

---

## 🚀 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Flask
* Git & GitHub

---

## 📊 Dataset

The dataset contains chemical properties of wine such as:

* Fixed Acidity
* Volatile Acidity
* Citric Acid
* Residual Sugar
* Chlorides
* Free Sulfur Dioxide
* Total Sulfur Dioxide
* Density
* pH
* Sulphates
* Alcohol

Target variable: **Wine Quality (Regression Problem)**

---

## 🔍 Exploratory Data Analysis (EDA)

* Alcohol and sulphates show positive correlation with quality
* Volatile acidity negatively impacts quality
* Target variable is slightly imbalanced (mostly 5–6)
* Some features contain outliers but are manageable

---

## 🤖 Model Building

* Baseline Model: Linear Regression (R² ≈ 0.40)
* Final Model: Random Forest Regressor (R² ≈ 0.54)

Evaluation Metrics:

* Mean Squared Error (MSE)
* R² Score

---

## ⚙️ Project Structure

wine-quality-project/
│
├── artifacts/
│   ├── model.pkl
│   └── scaler.pkl
│
├── src/
│   ├── pipeline/
│   │   └── predict_pipeline.py
│
├── app.py
├── requirements.txt
└── README.md

---

## 🧠 Pipeline

* Input features are scaled using StandardScaler
* Model predicts wine quality
* Output returned via Flask API

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

---

## 🔗 API Endpoint

### POST /predict

Example request:

```json
{
  "features": [7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4]
}
```

Example response:

```json
{
  "prediction": 5.3
}
```

---

## 📈 Key Learnings

* Built an end-to-end ML pipeline
* Understood importance of baseline models
* Applied model evaluation using RMSE and R²
* Learned Git workflow and deployment basics

---

## 🚀 Future Improvements

* Hyperparameter tuning using RandomizedSearchCV
* Try advanced models like XGBoost
* Deploy API on cloud (Render / AWS / GCP)

---

## 👩‍💻 Author

Vaidehi
