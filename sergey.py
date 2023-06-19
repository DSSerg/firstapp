import streamlit as st
import pandas as pd
import pickle
from sklearn import datasets


st.write("""
# Simple Iris Flower Prediction App
Clusterisation predict App
""")

st.sidebar.header('Ввод параметров')

def user_input_features():
    gender = st.sidebar.slider('Gender', 0, 1, 1)
    age = st.sidebar.slider('Age', 14, 90, 35)
    trans = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
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


#prediction = clf.predict(df)
#prediction_proba = clf.predict_proba(df)

#st.subheader('Class labels and their corresponding index number')
#st.write(iris.target_names)

#st.subheader('Prediction')
#st.write(iris.target_names[prediction])
#st.write(prediction)
