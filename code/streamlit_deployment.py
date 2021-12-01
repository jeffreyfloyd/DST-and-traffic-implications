import pickle
import requests
import folium
import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
from dateutil import parser
from branca.element import Figure
from streamlit_folium import folium_static

def get_weather(lat, lon):
    url = 'http://api.weatherapi.com/v1'
    slug = '/current.json'
    parameters = {
        'key': '0cb381c6bf3c4d4384b155640212911',
        'q': f'{lat},{lon}'
    }

    res = requests.get(url+slug, parameters)
    weather_data = res.json()
    
    condition_dict = {
        1000 : 'Clear',
        1006 : 'Cloudy',
        1135 : 'Fog',
        1171 : 'Freezing Rain',
        1201 : 'Freezing Rain',
        1195 : 'Heavy Rain',
        1192 : 'Heavy Rain',
        1243 : 'Heavy Rain',
        1246 : 'Heavy Rain',
        1225 : 'Heavy Snow',
        1117 : 'Heavy Snow',
        1114 : 'Heavy Snow',
        1258 : 'Heavy Snow',
        1222 : 'Heavy Snow',
        1153 : 'Light Drizzle',
        1150 : 'Light Drizzle',
        1168 : 'Light Freezing Drizzle',
        1072 : 'Light Freezing Drizzle',
        1147 : 'Light Freezing Fog',
        1198 : 'Light Freezing Rain',
        1261 : 'Light Ice Pellets',
        1237 : 'Light Ice Pellets',
        1264 : 'Light Ice Pellets',
        1153 : 'Light Rain',
        1183 : 'Light Rain',
        1240 : 'Light Rain Showers',
        1180 : 'Light Rain Showers',
        1213 : 'Light Snow',
        1255 : 'Light Snow',
        1210 : 'Light Snow',
        1204 : 'Light Snow and Sleet / Windy',
        1249 : 'Light Snow and Sleet / Windy',
        1207 : 'Light Snow and Sleet / Windy',
        1252 : 'Light Snow and Sleet / Windy',
        1069 : 'Light Snow and Sleet / Windy',
        1030 : 'Mist',
        1009 : 'Overcast',
        1003 : 'Partly Cloudy',
        1189 : 'Rain',
        1186 : 'Rain',
        1063 : 'Rain',
        1219 : 'Snow',
        1216 : 'Snow',
        1066 : 'Snow',
        1276 : 'Thunderstorms and Rain',
        1282 : 'Light Thunderstorms and Snow',
        1279 : 'Light Thunderstorms and Snow',
        1273 : 'Light Rain with Thunder',
        1087 : 'Thunder',
    }
        
    current_time = parser.parse(weather_data['location']['localtime'])
    current_weather = {
        'start_lat': float(lat),
        'start_lng': float(lon),
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
        f"weather_condition_{condition_dict[weather_data['current']['condition']['code']]}" : 1,
        f"day_{current_time.strftime('%A')}": 1,
        f"hour_{current_time.strftime('%H')}": 1
    }
    
    return current_weather

def prediction(weather_params):
        
    with open('./models/xgboost.pkl', mode='rb') as pickle_in:
        xg_model = pickle.load(pickle_in)
    with open('./models/xgboost_cols.pkl', mode='rb') as pickle_in:
        cols = pickle.load(pickle_in)
            
    pred_df = pd.DataFrame(columns=cols)
    pred_df = pred_df.append(weather_params, ignore_index=True).fillna(0)
    
    return xg_model.predict(pred_df)[0]

st.title('Accident Traffic Impact Prediction')

page = st.sidebar.selectbox('Select a page', ('About','Make a Prediction'))

if page == 'About':
    st.write('Can we predict how severely an accident will impact traffic based on location and weather conditions at the time it occurs?')

if page == 'Make a Prediction':
    
    city = st.selectbox('Select a City', ('Atlanta','Boston','Chicago','Denver'))
    if city == 'Atlanta':
        lattitude = 33.7490
        longitude = -84.3880
    elif city == 'Boston':
        lattitude = 42.3601
        longitude = -71.0589
    elif city == 'Chicago':
        lattitude = 41.8781
        longitude = -87.6298
    elif city == 'Denver':
        lattitude = 39.7392
        longitude = -104.9903
    
    weather_dict = get_weather(lattitude, longitude)
    
    lat_text = st.text_input('Lattitude Coordinate', value = f'{lattitude}')
    lon_text = st.text_input('Longitude Coordinate', value = f'{longitude}')
    
    severity_dict = {
        1 : 'Mild',
        2 : 'Moderate',
        3 : 'Severe',
        4 : 'Extreme'
    }
    
    if st.button('Predict!'):
        st.write(f'Predicted Traffic Impact is {severity_dict[prediction(weather_dict)]}')
    
    fig = Figure(width=550, height=350)
    m1 = folium.Map(width=550, height=350, location=[float(lat_text),float(lon_text)], zoom_start=10, max_zoom=16, min_zoom=8)
    fig.add_child(m1)
    folium.Marker(location=[float(lat_text),float(lon_text)], popup='marker 1').add_to(m1)
    folium_static(m1)
    
    

html_string = '<a href="https://www.weatherapi.com/" title="Free Weather API"><img src="//cdn.weatherapi.com/v4/images/weatherapi_logo.png" alt="Weather data by WeatherAPI.com" border="0"></a>'
st.markdown(html_string, unsafe_allow_html=True)

# if page == "":
#     st.write("")
#     name = st.checkbox('')
#     animal_type = st.selectbox('', [''])
#     age = st.slider('', 0.0, 20.0, step=0.1)
#     sex = st.multiselect('', ['',''])

#     if st.button(''):
#         outcome = prediction()
#         st.write(f"{outcome}")