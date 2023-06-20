import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
#import sklearn
#from sklearn import  KMeans
 
st.write("""
Clusterisation predict App
""")
#загрузка модели
clust = pickle.load(open("model3.pkl", "rb"))
st.sidebar.header('Ввод параметров')

def user_input_features():
    gender = st.sidebar.slider('Gender (0 - female, 1 - male)', 0, 1, 1)
    age = st.sidebar.slider('Age', 14, 50, 35)
    trans = st.sidebar.slider('Transactions', 0.0, 10000.0, 100.0)
    bal=st.sidebar.slider("Balance', 0.0, 20000.0, 1000.0)
    data = {'CustGender': gender,
            'TransactionAmount (BYN)': trans,
            'Age': age}
    features = pd.DataFrame(data, index=[0])
    return features

dff = user_input_features()

st.subheader('Введенные параметры')
st.write(dff)
result=clust.predict(dff)
#st.write(dff)
st.write("Клиент относится к кластеру:", (result-dff['CustGender']))

