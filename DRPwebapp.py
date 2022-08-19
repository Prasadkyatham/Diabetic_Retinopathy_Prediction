# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 17:09:01 2022

@author: HRITHIK
"""

import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('gbc_model_pickle', 'rb'))

# creating a function for Prediction

from PIL import Image
image = Image.open("Diabetic_Retinopathy1.jpg")
st.image(image)

def diabeticreti_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return "You Are Not Suffering From Diabetic Retinopathy"
    else:
      return "You Are Suffering From Diabetic Retinopathy"
  
    
def main():
      # giving a title
 
    html_temp="""
    <div style ="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetic Retinopathy Prediction app 
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True) 
    
    # getting the input data from the user
    	
    
    age = st.text_input('Age of the Person',"Type Here")
    systolic_bp = st.text_input("Systolic BP value","Type Here")
    dystolic_bp = st.text_input("Dystolic BP value","Type Here")
    cholesterol = st.text_input("Cholesterol value","Type Here")
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Predict'):
        diagnosis = diabeticreti_prediction([age, systolic_bp, dystolic_bp, cholesterol])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    
    
    