import numpy as np
import pickle
import pandas as pd
import streamlit as st

pickle_in =open('RFModel.pkl','rb')
RFModel = pickle.load(pickle_in)



def main():
    st.title("Real Estate Housing Prediction in California ")
    st.header("Estimating the House Price of a particular location in California ")
    html_temp = """
    <div style="background-color:blue ;padding:10px">
    <h2 style="color:white;text-align:center;">Real Estate Housing Price Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)


    longitude = st.slider("longitude",-125,-114,-118)
    latitude = st.slider("latitude",32,42,34)
    housing_median_age = st.slider("housing_median_age",1,52,29)
    total_rooms = st.number_input("total_rooms",2,39320,2124)
    median_income= st.number_input("median_income",0,15,3)
    ocean_proximity= st.number_input("ocean_proximity", 0,4,1)
    
    result=""
    if st.button("Predict"):
        result=predict_house_price(longitude,latitude,housing_median_age,total_rooms,median_income,ocean_proximity)
        st.success('The Price of House is $ {}'.format(result[0]))
  

def predict_house_price(longitude,latitude,housing_median_age,total_rooms,median_income,ocean_proximity):
    """Let's Predict The predict_house_price
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: longitude
        in: query
        type: number
        required: true
      - name: latitude
        in: query
        type: number
        required: true
      - name: housing_median_age
        in: query
        type: number
        required: true
      - name: total_rooms
        in: query
        type: number
        required: true
      - name: median_income
        in: query
        type: number
        required: true
      - name: ocean_proximity
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=RFModel.predict([[longitude,latitude,housing_median_age,total_rooms,median_income,ocean_proximity]])
    print(prediction)
    return prediction


if __name__ == '__main__':
    main()