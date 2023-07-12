import streamlit as st
import eda
import prediction


# Set Config dan icon
st.set_page_config(
        page_title='Plant Nutrition Prediction',
        layout='wide',
        )

# Hide Streamlit Style
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# Membuat navigasi
navigation = st.sidebar.selectbox('Pilih Halaman (Plant Nutrition Prediction/EDA): ', ('Plant Nutrition Prediction','Exploratory Data Analysis'))
st.sidebar.image("https://imgur.com/FZTgNj9.png", use_column_width=True)

# Run modul dengan if else
if navigation == 'Plant Nutrition Prediction' :
    prediction.run()
else :
    eda.run()