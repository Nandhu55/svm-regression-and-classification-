import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder

# Load trained model
model = pickle.load(open("student_svm_model.pkl", "rb"))

# Title
st.title("Student Performance Prediction")

st.write("Enter student details below")

# Input Fields
study_hours = st.number_input(
    "Study Hours",
    min_value=1,
    max_value=12,
    value=5
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0,
    max_value=100,
    value=75
)

assignments_completed = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=20,
    value=10
)

previous_marks = st.number_input(
    "Previous Marks",
    min_value=0,
    max_value=100,
    value=60
)

internet_access = st.selectbox(
    "Internet Access",
    ["Yes", "No"]
)

extra_classes = st.selectbox(
    "Extra Classes",
    ["Yes", "No"]
)

parent_support = st.selectbox(
    "Parent Support",
    ["Low", "Medium", "High"]
)

# Encode categorical values
internet_access_encoded = 1 if internet_access == "Yes" else 0

extra_classes_encoded = 1 if extra_classes == "Yes" else 0

parent_support_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

parent_support_encoded = parent_support_mapping[parent_support]

# Predict Button
if st.button("Predict"):

    input_data = np.array([[
        study_hours,
        attendance,
        assignments_completed,
        previous_marks,
        internet_access_encoded,
        extra_classes_encoded,
        parent_support_encoded
    ]])

    prediction = model.predict(input_data)

    # Output
    if prediction[0] == 1:
        st.success("Prediction: Pass")
    else:
        st.error("Prediction: Fail")