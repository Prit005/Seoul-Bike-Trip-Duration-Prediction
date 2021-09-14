import joblib
import matplotlib as plt
import pandas as pd
import numpy as np
import os
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GridSearchCV
 
# Captures the path of current folder
curr_path = os.path.dirname(os.path.realpath(__file__))

feature_coloumns = ['Haversine', 'Trip_Distance', 'Pickup_month', 'Pickup_day', 'Pickup_hour', 
                   'Pickup_minute','Pickup_day_of_week', 'Pickup_Long', 'Pickup_Latd', 
                   'Drop_month', 'Drop_day', 'Drop_hour', 'Drop_minute', 'Drop_day_of_week',
                   'Drop_Long','Drop_Latd','Temperature','Percipitation','Windspeed','Humidity',
                   'Solar_radiation', 'Snowfall','Ground_Temperature','One_average_dust']

gbdt_final = joblib.load(curr_path + "/final_model_best.joblib")

print(gbdt_final)

def predict_duration(attributes: np.array):
    """ Returns Bike Trip Duration value"""
    
    pred = gbdt_final.predict(attributes)
    print("Duration predicted")

    return int(pred[0])