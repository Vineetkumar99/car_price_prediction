import numpy as np
import pandas as pd
import streamlit as st
import pickle
import sklearn
# Import the Model
pipe=pickle.load(open('LinearRegressionModel.pkl','rb'))
df=pickle.load(open('cleaned_car.pkl','rb'))

st.title("Car Price Predictor")

#Company Name

company=st.selectbox("Select Company:",df["company"].unique())

#Model
car_model=st.selectbox("Select Model:",df["name"].unique())

#Year
year=st.selectbox("Select Year:",sorted(df["year"].unique()))

#Fuel_type
fuel_type=st.selectbox("Select Fuel_type:",df["fuel_type"].unique())

#kilometers_travelled

kms_driven= st.number_input('Enter Number of Kilometers Travelled:')

if st.button('Predict Price'):
    year=int(year)
    kms_driven=int(kms_driven)

    prediction=pd.DataFrame({'company':[company],'name':[car_model],'year':[year],'fuel_type':[fuel_type],'kms_driven':[kms_driven]})
    #st.table(prediction)
    result=pipe.predict(prediction)
    st.header("The Predicted Price of Car is:" + "  "+str(int(result)))

