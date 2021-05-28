import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import pytz
import requests

'''
# Taxi Fare Calculator
'''

nyc_datetime_now = datetime.now(pytz.timezone('Europe/Lisbon'))
d = st.date_input("Pickup date", datetime.date(nyc_datetime_now))
t = st.time_input('Pickup time', datetime.time(nyc_datetime_now))

pickup_datetime = datetime.combine(d, t).strftime("%Y-%m-%d %H:%M:%S")
pickup_longitude = st.text_input("Pickup longitude", 40.7614327)
pickup_latitude = st.text_input("Pickup latitude", -73.9798156)
dropoff_longitude = st.text_input("Dropoff longitude", 40.7614327)
dropoff_latitude = st.text_input("Dropoff latitude", -73.9798156)
passenger_count = st.slider('Number of passengers', 1, 10, 3)


url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url=url, params=params).json()
prediction = round(response['prediction'], 2)

st.write(f"**This trip will cost you {prediction} €**")
