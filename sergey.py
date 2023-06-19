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

st.sidebar.header('Ввод параметров')

def user_input_features():
    gender = st.sidebar.slider('Gender (0 - female, 1 - male)', 0, 1, 1)
    age = st.sidebar.slider('Age', 14, 70, 35)
    trans = st.sidebar.slider('Transactions', 0, 50000, 1000)
    data = {'CustGender': gender,
            'TransactionAmount (BYN)': trans,
            'Age': age}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Введенные параметры')
st.write(df)

#загрузка модели
#pickle_in = open('model.pkl', 'rb')
#clust = pickle.load(open("https://drive.google.com/file/d/1oUBUar4jsVNr9VnNNT0LAtkZfdzWprjs/view?usp=sharing", "rb"))
clust = pickle.load(open("model.pkl", "rb"))
#to_predict=np.array(gender,age,trans)
result=clust.predict(df)

st.write("кластер=", result)

