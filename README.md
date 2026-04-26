# 🚢 Titanic Survival Prediction

## 📌 Project Overview

This project predicts whether a passenger survived the Titanic disaster using machine learning techniques. It covers the complete ML pipeline from data preprocessing to model deployment.

---

## 🎯 Objectives

* Analyze the Titanic dataset using exploratory data analysis (EDA)
* Perform data cleaning and feature engineering
* Train and compare multiple machine learning models
* Optimize the best-performing model
* Deploy the model using a Streamlit web application

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
* **Machine Learning:** Scikit-learn
* **Deployment:** Streamlit

---

## 📊 Project Workflow

### 1. Data Cleaning & EDA

* Handled missing values (Age, Embarked)
* Removed irrelevant columns (Cabin)
* Visualized survival patterns based on gender and class

### 2. Feature Engineering

* Created **FamilySize** feature
* Derived **Age Groups** (Adult, Senior)
* Encoded categorical variables

### 3. Model Building

* Trained multiple models:

  * Logistic Regression
  * Random Forest
  * Decision Tree
* Compared performance using accuracy

### 4. Model Optimization

* Applied **GridSearchCV** for hyperparameter tuning
* Selected the best-performing model

### 5. Deployment

* Built an interactive web app using Streamlit
* Users can input passenger details and get predictions

---

## 📈 Results

* **Best Model:** Random Forest Classifier
* **Accuracy:** 82.5%

---

## 🌐 Live Demo

Will be updated after deployment

---

## 📁 Project Structure

```
Titanic-Survival-Prediction/
│
├── model/
│   └── models.pkl
├── app.py
├── datacleaning.ipynb
├── modelbuilding.ipynb
├── titanic_cleaned.csv
├── Titanic-Dataset.csv
├── README.md
└── requirements.txt
```

---

## 💡 Key Learnings

* Importance of data preprocessing and feature engineering
* Model comparison and performance evaluation
* Hyperparameter tuning techniques
* Ensuring consistency between training and prediction pipelines
* Building and deploying ML applications

---

## 🚀 Future Improvements

* Improve model accuracy with advanced algorithms
* Add more features for better prediction
* Enhance UI/UX of the web application
* Deploy using cloud platforms (AWS, GCP)

---

## 🙌 Acknowledgement

Dataset sourced from the Titanic dataset (commonly used in ML practice).

---

## 📬 Contact

Feel free to connect with me for collaboration or feedback.
