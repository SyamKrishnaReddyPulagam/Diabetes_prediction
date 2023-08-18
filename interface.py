import streamlit as st
import pandas as pd
import numpy as np
import pickle

loaded_model = pickle.load(open('Diabetes_prediction.pkl', 'rb'))
sc = pickle.load(open('sc.pkl', 'rb'))

st.title("DIABETES PREDICTION")
st.header("Prediction")
st.header("PREDICT WHETHER YOU ARE EFFECTED BY DIABETES")
Pregnancies=st.number_input("Pregnancies",min_value=0.0,max_value=17.0,value=0.0,step=1.0)
Pregnancies=int(Pregnancies)
Glucose=st.number_input("Glucose",min_value=0.0,max_value=199.0,value=0.0,step=1.0)
Glucose=int(Glucose)
BloodPressure=st.number_input("BloodPressure",min_value=0.0,max_value=122.0,value=0.0,step=1.0)
BloodPressure=int(BloodPressure)
SkinThickness=st.number_input("SkinThickness",min_value=0.0,max_value=99.0,value=0.0,step=1.0)
SkinThickness=int(SkinThickness)
Insulin=st.number_input("Insulin",min_value=0.0,max_value=846.0,value=0.0,step=1.0)
Insulin=int(Insulin)
BMI=st.number_input("BMI",min_value=0.0,max_value=67.1,value=0.0,step=0.1)
DiabetesPedigreeFunction=st.number_input("DiabetesPedigreeFunction",min_value=0.078000,max_value=2.42,value=0.078000,step=0.1)
Age=st.number_input("Age",min_value=1.0,max_value=81.0,value=1.0,step=1.0)
Age=int(Age)
if st.button("PREDICT"):
        classifier=loaded_model.predict(sc.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]]))
        if classifier == 0:
            st.success("NOT EFFECTED BY DIABETES!")
            st.write("<span style='font-size: 30px;'>YOU ARE HEALTHY</span>", unsafe_allow_html=True)
        else:
            st.error("YOU ARE EFFECTED BY DIABETES!")
            st.write("<span style='font-size: 30px;'>PLEASE CONSULT DOCTOR</span>", unsafe_allow_html=True)
st.write("")	
st.write("A PROJECT BY")
st.markdown("<h1 style='font-size: 20px;'>SYAM KRISHNA REDDY PULAGAM</h1>", unsafe_allow_html=True)