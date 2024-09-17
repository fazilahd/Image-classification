import streamlit as st
import numpy as np
import joblib

st.title("Bike Purchasement Prediction App")

st.divider()

income=st.number_input("Enter the income", min_value=0, value=30000)
age=st.number_input("Enter your age", min_value=15, value=30)
education=st.number_input("Enter the Education", min_value=0, value=2)
homeowner=st.number_input("Homeowner input", min_value=0, value=1)

model=joblib.load("model.pkl")

X=[income, age, education, homeowner]

st.divider()

predictbutton=st.button("Press for prediction of bike purchasement")

st.divider()

if predictbutton:
    st.balloons()
    X1=np.array([X])
    prediction=model.predict(X1)[0]
    result = "Customer will purchase" if prediction == 1 else "Customer won't purchase"
    st.write(result)
else:
    st.write("Please enter values and use predict button")



