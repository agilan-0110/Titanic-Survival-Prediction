import streamlit as st
import numpy as np
import pickle

# Load trained model
model = pickle.load(open("model/models.pkl", "rb"))

# Title
st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival")

# -------------------------------
# 🧾 USER INPUTS (MINIMIZED)
# -------------------------------

pclass = st.selectbox("Passenger Class", ["1st", "2nd", "3rd"])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 0, 80, 25)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)
sibsp = st.number_input("Siblings/Spouses", 0, 5, 0)
parch = st.number_input("Parents/Children", 0, 5, 0)
embarked = st.selectbox(
    "Boarding Port",
    ["Cherbourg (France)", "Queenstown (Ireland)", "Southampton (England)"]
)
# -------------------------------
# 🔄 DATA TRANSFORMATION
# -------------------------------

# Convert class
pclass = {"1st": 1, "2nd": 2, "3rd": 3}[pclass]

# Convert sex
sex = 0 if sex == "Male" else 1

# Feature Engineering
family_size = sibsp + parch + 1

# Age Group Encoding
if age < 18:
    age_adult = 0
    age_senior = 0
elif age < 60:
    age_adult = 1
    age_senior = 0
else:
    age_adult = 0
    age_senior = 1

# Embarked Encoding
if "Cherbourg" in embarked:
    embarked_Q = 0
    embarked_S = 0
elif "Queenstown" in embarked:
    embarked_Q = 1
    embarked_S = 0
else:
    embarked_Q = 0
    embarked_S = 1

# -------------------------------
# 🤖 PREDICTION
# -------------------------------

if st.button("Predict"):
    input_data = np.array([[
        pclass,
        sex,
        age,
        sibsp,
        parch,
        fare,
        family_size,
        age_adult,
        age_senior,
        embarked_Q,
        embarked_S
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Passenger Survived")
    else:
        st.error("❌ Passenger Did Not Survive")