import pickle

import numpy as np
import streamlit as st

knn_model = pickle.load(open("knn_model.pkl", "rb"))
logistic_model = pickle.load(open("logistic_model.pkl", "rb"))


st.title("Placement Hoga Ya Nahi?")
st.text("using k-Nearest Neighbor and Logistic Regression")

iq = st.number_input("Enter your IQ")
cgpa = st.number_input("Enter your CGPA")

def predict_placement():
    input_data = np.array([[cgpa, iq]])
    knn_prediction = knn_model.predict(input_data)
    logistic_prediction = logistic_model.predict(input_data)

    return knn_prediction, logistic_prediction

if st.button("Predict"):
    knn_result, logistic_result = predict_placement()

    st.write(f"KNN Prediction: {'Mubarak ho, Google pakka' if knn_result[0] == 1 else 'Dekha laparvahi ka natija'}")
    st.write(f"Logistic Regression Prediction: {'Mubarak ho, Google pakka' if logistic_result[0] == 1 else 'Dekha laparvahi ka natija'}")

