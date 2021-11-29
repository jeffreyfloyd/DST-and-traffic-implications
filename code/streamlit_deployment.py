import streamlit as st
import pickle
import numpy as np
import tensorflow as tf
import pydeck as pdk
import requests

st.title('Accident Severity Prediction')

page = st.sidebar.selectbox('Select a page', ('About','Make a Prediction'))

if page == 'About':
    st.write('Can we predict the severity of an accident based on certain conditions at the time of the accident?')

if page == 'Make a Prediction':
    lat_text = st.text_input('Lattitude Coordinate', value = '41.8781')
    lon_text = st.text_input('Longitude Coordinate', value = '-87.6298')
    
    if st.button('tell me the weather'):
        url = 'http://api.weatherapi.com/v1'
        slug = '/current.json'
        parameters = {
            'key': '0cb381c6bf3c4d4384b155640212911',
            'q': f'{lat_text},{lon_text}'
        }

        res = requests.get(url+slug, parameters)
        weather_data = res.json()
        st.write(f'{weather_data}')
    
    with open('./models/xgboost.pkl', mode='rb') as pickle_in:
        xg_model = pickle.load(pickle_in)

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