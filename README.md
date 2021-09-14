# Seoul-Bike-Trip-Duration-Prediction

Description - Trip duration is the most fundamental measure in all modes of transportation.
Hence, it is crucial to predict the trip-time precisely for the advancement of Intelligent
Transport Systems (ITS) and traveller information systems. In order to predict the trip
duration, data mining techniques are employed in this paper to predict the trip duration of
rental bikes in Seoul Bike sharing system. The prediction is carried out with the combination
of Seoul Bike data and weather data. The Data used include trip duration, trip distance,
pickup-drop-off latitude and longitude, temperature, precipitation, wind speed, humidity, solar
radiation, snowfall, ground temperature and 1-hour average dust concentration.

**Performance Metric:-** Root Mean Square Error, Mean Absolute Error, Median Absolute Error, R2_Score  

## Dataset:- Download from [**here**](https://www.kaggle.com/saurabhshahane/seoul-bike-trip-duration-prediction).
## Dataset Details
![data](data_dict_seoul.jpeg)

# TASK!!
## 1. EDA
## 2. Data Pre-processing
## 3. Feature Engineering
## 4. Preprocessing Data:- [**here**](https://drive.google.com/file/d/1OLegVzjnChgqf82D459d0qTrs--M81Pc/view?usp=sharing)

## 5. Machine Learning Algorithms:-
###    * Baseline Model
           1) LinearRegression

###    * Ensemble Model with HyperParameterTuning
           1) RandomForestRegressor
           2) DecisionTreeRegressor
           3) GradientBoostingRegressor
           4) XGBRegressor
           5) LGBM

From this Baseline Model and Ensemble Models, we choose **GradientBoostingRegressor** as a **Best** Model.
## HyperparameterTuning Best Parameters are:

          The Best Parameters are :  **{'learning_rate': 1, 'max_depth': 3}**

**GradientBoostingRegressor results**

          **************************************************
          Train Root Mean squared error: **6.74**

          CV Root Mean squared error: **6.92**

          Test Root Mean squared error: **6.88**
          **************************************************
          Train Mean Absolute error:  **4.176270876136381**

          CV Mean Absolute error:  **4.195389887259278**

          Test Mean Absolute error:  **4.20950943388566**
          **************************************************
          Train Median Absolute error:  **2.641925216618098**

          CV Median Absolute error:  **2.6439486001698356**

          Test Median Absolute error:  **2.6603131416873396**
          **************************************************
          Train r2_score error:  **0.9274254192232534**

          CV r2_score error:  **0.9234346774166566**

          Test r2_score error:  **0.9244233138181509**
          **************************************************

### Feature Importance
![image](https://user-images.githubusercontent.com/69208280/133316238-c0707ad6-e743-4fdf-894c-d8c5c469fbdd.png)

# Deployment Link: - https://seoulbiketripdurationpred.herokuapp.com/.
# Video Link: - [**here**](https://drive.google.com/file/d/1VO3ENntYdhsSVLJGHCLpAefoa0J8r9PV/view?usp=sharing)
