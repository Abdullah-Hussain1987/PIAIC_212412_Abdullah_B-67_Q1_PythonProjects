# PIAIC212412
# Abdullah Hussain
# Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes

import streamlit as st
import pandas as pd

st.title('BMI Calculator')
st.subheader('Enter your Details')

height = st.slider("Enter your height in cm:", 100, 350, 150)
weight = st.slider("Enter your weight in Kg:", 15, 250, 50)

bmi = weight/((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("BMI Cateogories")
st.write("Underweight: BMI less than 18.5")
st.write("Normal: BMI between 18.5 and 24.9")
st.write("Overweight: BMI between 25 and 29.9")
st.write("Obesity: BMI 30 or above")