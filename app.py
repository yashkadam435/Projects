import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
from keras.models import load_model
import streamlit as st

st.title('Stock Market Prediction')
user_input = st.text_input('Enter Stock Ticker', 'Enter Ticker') 
df = pdr.get_data_tiingo('AAPL', api_key = "4b02afe8c6b9cb1c67dffc27f73a9a98195270af")

#Describing Data
st.subheader('Data from 2017 - 2022')
st.write(df.describe())
st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.close.to_numpy())
st.pyplot(fig)
