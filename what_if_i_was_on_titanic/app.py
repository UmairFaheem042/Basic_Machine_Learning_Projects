import streamlit as st
import pickle
import pandas as pd

lrg_model = pickle.load(open("lrg_model.pkl", "rb"))
knn_model = pickle.load(open("knn_model.pkl", "rb"))
svm_model = pickle.load(open("svm_model.pkl", "rb"))
rfc_model = pickle.load(open("rfc_model.pkl", "rb"))

st.header("What If I was on Titanic")
st.text("Predict whether I would survive or not using IcebergAhead")

family_members = st.number_input("Enter Family Members: ", min_value=0, step=1, format="%d")
passenger_age = st.number_input("Enter Age: ",  min_value=0, step=1, format="%d")
passenger_class = st.radio("Choose your Passenger Class: ", ["First", "Second", "Third"],)
boarding_station = st.radio("Choose your Boarding Station: ", ["Cherbourg", "Southampton", "Queesntown"],)
passenger_gender = st.radio("Choose your Gender: ", ["Male", "Female"],)



def prepare_inputs():
    if passenger_class == 'First':
        pclass = 1
    elif passenger_class == 'Second':
        pclass = 2
    else:
        pclass = 3

    if boarding_station == 'Cherbourg':
        embarked_C = 1
        embarked_Q = 0
        embarked_S = 0
    elif boarding_station == 'Southampton':
        embarked_C = 0
        embarked_Q = 0
        embarked_S = 1
    else:
        embarked_C = 0
        embarked_Q = 1
        embarked_S = 0

    if passenger_gender == 'Male':
        sex_male = 1
    else:
        sex_male = 0

    input_data = pd.DataFrame({
        'Pclass': [pclass],
        'Age': [passenger_age],
        'Family': [family_members],
        # 'Embarked_C': [embarked_C],
        'Embarked_Q': [embarked_Q],
        'Embarked_S': [embarked_S],
        'Sex_male': [sex_male]
    })

    return input_data


if st.button("Predict"):
    input_data = prepare_inputs()

    # predicting using models
    lrg_pred = lrg_model.predict(input_data)
    knn_pred = lrg_model.predict(input_data)
    svm_pred = lrg_model.predict(input_data)
    rfc_pred = lrg_model.predict(input_data)

    st.subheader("Predictions")
    st.text(f"Logistic Regression: {'Survived' if lrg_pred[0] == 1 else 'Not Survived'}")
    st.text(f"k-Nearest Neighbor: {'Survived' if knn_pred[0] == 1 else 'Not Survived'}")
    st.text(f"Support Vector Machine: {'Survived' if svm_pred[0] == 1 else 'Not Survived'}")
    st.text(f"Random Forest Classifier: {'Survived' if rfc_pred[0] == 1 else 'Not Survived'}")