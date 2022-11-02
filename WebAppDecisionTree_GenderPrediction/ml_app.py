# use streamlit run ml_app.py on terminal

import streamlit as st
import pickle

st.title("Gender prediction using Decision tree classifier")

# weight = st.number_input("Enter weight", 0, 150)
# height = st.number_input("Enter height", 0, 200)
w = st.slider("Enter weight", 1, 120)
h = st.slider("Enter height", 50, 200)

loadedModel = pickle.load(open('finalmodel.pkl', 'rb'))

# pred = loadedModel.predict([[weight, height]])
pred = loadedModel.predict([[w, h]])

st.write("The gender of person is ", pred[0])