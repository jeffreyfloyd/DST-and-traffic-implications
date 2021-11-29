import streamlit as st
import pickle
import numpy as np
import tensorflow as tf

st.title('Accident Severity Prediction')

page = st.sidebar.selectbox('Select a page', ('About','Make a Prediction'))

if page == 'About':
    st.write('Can we predict the severity of an accident based on certain conditions at the time of the accident?')

if page = 'Make a Prediction':
    model_type = st.selectbox('Select a Model Type', ['XGBoost','BAG','Neural Net'])

def prediction():
    return

# <a href="https://www.weatherapi.com/" title="Free Weather API"><img src='//cdn.weatherapi.com/v4/images/weatherapi_logo.png' alt="Weather data by WeatherAPI.com" border="0"></a>

# if page == "":
#     st.write("")
#     name = st.checkbox('')
#     animal_type = st.selectbox('', [''])
#     age = st.slider('', 0.0, 20.0, step=0.1)
#     sex = st.multiselect('', ['',''])

#     if st.button(''):
#         outcome = prediction()
#         st.write(f"{outcome}")