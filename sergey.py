import streamlit as st
import pandas as pd
import pickle
#from sklearn import datasets


st.write("""
Clusterisation predict App
""")

st.sidebar.header('Ввод параметров')

def user_input_features():
    gender = st.sidebar.slider('Gender', 0, 1, 1)
    age = st.sidebar.slider('Age', 14, 90, 35)
    trans = st.sidebar.slider('Transactions', 0.0, 100000, 1000)
    data = {'gender': gender,
            'age': age,
            'trans': trans}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Ввод параметров')
st.write(df)

#загрузка модели
pickle_in = open('model.pkl', 'rb')
clust = pickle.load(pickle_in)



