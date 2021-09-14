import streamlit as st
import joblib
import numpy as np
import os
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
from model import predict_duration

st.set_page_config(page_title="SEOUL BIKE TRIP DURATION PREDICT APP", page_icon="🛴", layout="wide")

with st.form("prediction_form"):
    st.header("Enter Details for Trip Duration Prediction")

    Haversine = st.number_input("Haversine",format="%f")
    Trip_Distance = st.number_input("Trip_Distance",value=0,format="%d")
    Pickup_month = st.slider("Pickup_month",1,12,value=1,format="%d")
    Pickup_day = st.slider("Pickup_day",1,31,value=1,format="%d")
    Pickup_hour = st.slider("Pickup_hour",0,24,value=0,format="%d")
    Pickup_minute = st.slider("Pickup_minute",0,60,value=0,format="%d")
    Pickup_day_of_week = st.slider("Pickup_day_of_week",0,6,value=0,format="%d")
    Pickup_Long = st.number_input("Pickup_Long")
    Pickup_Latd = st.number_input("Pickup_Latd")
    Drop_month = st.slider("Drop_month",1,12,value=1,format="%d")
    Drop_day = st.slider("Drop_day",1,31,value=1,format="%d")
    Drop_hour = st.slider("Drop_hour",0,24,value=0,format="%d")
    Drop_minute = st.slider("Drop_minute",0,60,value=0,format="%d")
    Drop_day_of_week = st.slider("Drop_day_of_week",0,6,value=0,format="%d")
    Drop_Long = st.number_input("Drop_Long")
    Drop_Latd = st.number_input("Drop_Latd")
    Temperature = st.number_input("Temperature")
    Percipitation = st.number_input("Percipitation")
    Windspeed = st.number_input("Windspeed")
    Humidity = st.number_input("Humidity")
    Solar_radiation = st.number_input("Solar_radiation")
    Snowfall = st.number_input("Snowfall")
    Ground_Temperature = st.number_input("Ground_Temperature")
    One_average_dust = st.number_input("One_average_dust")
    submit_val = st.form_submit_button("PREDICT DURATION")

if submit_val:
    # If submit is pressed == True
    attribute = np.array([Haversine,Trip_Distance, Pickup_month, Pickup_day, Pickup_hour, 
                   Pickup_minute, Pickup_day_of_week, Pickup_Long,Pickup_Latd, 
                   Drop_month, Drop_day, Drop_hour, Drop_minute, Drop_day_of_week, Drop_Long,Drop_Latd,
                   Temperature,Percipitation,Windspeed,Humidity,Solar_radiation,
                   Snowfall,Ground_Temperature, One_average_dust]).reshape(1,-1)


    if attribute.shape == (1,24):
        print("attrubutes valid")
        

        value = predict_duration(attributes = attribute)

        st.header("Predicted Results:")
        st.success(f"The predicted Duration is {value} mins")














