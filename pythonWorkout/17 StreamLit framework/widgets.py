import streamlit as st
import pandas as pd

st.title("Exercising the widgets and text inputs")

name = st.text_input("Enter your name : ")
age = st.slider("Select your age", 0,100,25)

gender_options = ['Male','Female','Others']
gender_choice = st.selectbox("select your gender : ",gender_options)

# to upload a file component
uploaded_file = st.file_uploader("Drop your .csv file here", type = 'csv')
if uploaded_file is not None:
    df = pd.DataFrame(uploaded_file)


if name:
    st.write(f"Hello, {name}! ")
st.write(f"Your age is {age}. !!")
st.write(f"To verify, your gender is  : {gender_choice}")