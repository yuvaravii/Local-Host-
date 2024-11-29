import pandas as pd # type: ignore
import numpy as np
import streamlit as st # type: ignore

# for creating title in streamlit web app
st.title("Welcome to Streamlit web app")

# Trying to display the simple text
st.write("This is simple list")

# creating a dataframe from pandas 
df = pd.DataFrame(
{    
    "firstCol" : [1,2,3,4],
    "secondCol" : [10,20,30,40]
}
)

st.write("Here is the dataframe")
st.write(df)

# creating a line chart 
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)
