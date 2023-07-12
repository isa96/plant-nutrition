import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn

# Load Model
with open('model_opt.pkl', 'rb') as file_1:
  model_opt = pickle.load(file_1)

def run() :
    # Membuat Title 
    st.markdown("<h1 style='text-align: center;'>Plant Nutrition Prediction</h1>", unsafe_allow_html=True)
    st.write('Page ini berisi model untuk prediksi nutrisi tanaman dengan 8 variable dan sample_type. Mohon persiapkan data terlebih dahulu sebelum melakukan prediksi')

    # Membuat Form
    with st.form(key= 'form_plant'):
        st.markdown('## **Variable**')
        v1 = st.number_input('**V1**', min_value=227.28, max_value= 678.37, value=295.16 ,step=1.,format="%.2f")
        v2 = st.number_input('**V2**', min_value=178.80, max_value= 422.81, value=204.18 ,step=1.,format="%.2f")
        v3 = st.number_input('**V3**', min_value=348.93, max_value= 722.31, value=414.38 ,step=1.,format="%.2f")
        v4 = st.number_input('**V4**', min_value=313.73, max_value= 558.50, value=370.74 ,step=1.,format="%.2f")
        v5 = st.number_input('**V5**', min_value=373.33, max_value= 721.00, value=456.03 ,step=1.,format="%.2f")
        v6 = st.number_input('**V6**', min_value=189.20, max_value= 415.37, value=226.06 ,step=1.,format="%.2f")
        v7 = st.number_input('**V7**', min_value=586.26, max_value= 853.46, value=718.83 ,step=1.,format="%.2f")
        v8 = st.number_input('**V8**', min_value=3725.66, max_value= 5086.37, value=4554.76 ,step=1.,format="%.2f")
        st.markdown('---')
        sample_type = st.selectbox('Sample Type',('lab 1','lab 2'),index=1)
        submitted = st.form_submit_button('Predict')

    # Membuat Dataframe
    data_inf = {
        'v1' : v1, 
        'v2' : v2, 
        'v3' : v3, 
        'v4' : v4, 
        'v5' : v5, 
        'v6' : v6,
        'v7' : v7, 
        'v8' : v8,
        'sample_type' : sample_type
    }
    data_inf = pd.DataFrame([data_inf])
    data_inf

    # Prediksi
    if submitted :
        # Predict using Random Forest Parameter Tuning
        y_pred_inf = model_opt.predict(data_inf)
        st.write('# **Plant Nutrition Prediction :** ',y_pred_inf[0])

if __name__ == '__main__':
    run()