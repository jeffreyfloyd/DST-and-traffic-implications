import streamlit as st
import pickle
import numpy as np
import pandas as pd
import tensorflow as tf
import pydeck as pdk
import requests
import datetime as dt
from dateutil import parser

st.title('Accident Severity Prediction')

page = st.sidebar.selectbox('Select a page', ('About','Make a Prediction'))

if page == 'About':
    st.write('Can we predict the severity of an accident based on certain conditions at the time of the accident?')

if page == 'Make a Prediction':
    lat_text = st.text_input('Lattitude Coordinate', value = '41.8781')
    lon_text = st.text_input('Longitude Coordinate', value = '-87.6298')
    
    if st.button('Predict!'):
        url = 'http://api.weatherapi.com/v1'
        slug = '/current.json'
        parameters = {
            'key': '0cb381c6bf3c4d4384b155640212911',
            'q': f'{lat_text},{lon_text}'
        }

        res = requests.get(url+slug, parameters)
        weather_data = res.json()
        
        current_time = parser.parse(weather_data['location']['localtime'])
        prediction_params = {
            'start_lat': float(lat_text),
            'start_lng': float(lon_text),
            'temperature(f)': weather_data['current']['temp_f'],
            'wind_chill(f)': weather_data['current']['feelslike_f'],
            'humidity(%)': weather_data['current']['humidity'],
            'pressure(in)': weather_data['current']['pressure_in'],
            'visibility(mi)': weather_data['current']['vis_miles'],
            'wind_speed(mph)': weather_data['current']['wind_mph'],
            'precipitation(in)': weather_data['current']['precip_in'],
            'year': current_time.strftime('%Y'),
            'month': current_time.strftime('%m'),
            'week': current_time.strftime('%U'),
            'start_time_ep': (current_time - dt.datetime(1970,1,1)).total_seconds(),
            f"wind_direction_{weather_data['current']['wind_dir']}": 1,
            f"day_{current_time.strftime('%A')}": 1,
            f"hour_{current_time.strftime('%H')}": 1
        }
    
        with open('./models/xgboost.pkl', mode='rb') as pickle_in:
            xg_model = pickle.load(pickle_in)
        with open('./models/xgboost_cols.pkl', mode='rb') as pickle_in:
            cols = pickle.load(pickle_in)
            
        pred_df = pd.DataFrame(columns=cols)
        pred_df = pred_df.append(prediction_params, ignore_index=True).fillna(0)
        st.write(f'Predicted Traffic Severity is {xg_model.predict(pred_df)[0]}')
        

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