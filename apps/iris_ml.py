import streamlit as st
import pandas as pd
from PIL import Image 
import requests

from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

def app():
    
    st.title('Iris Classification')
    url = 'https://images.unsplash.com/photo-1561831220-cc44b32786ca?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1050&q=80'
    image = Image.open(requests.get(url, stream=True).raw)

    st.image(image, use_column_width=True)

    st.write("""
    # Simple Iris Flower Prediction App

    This app predicts the **Iris flower** type!
    """)

    st.sidebar.header('Iris Flower - User Input Parameters')

    def sidebar_input():
        # get data from sidebar slider for sepal/petal
        sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
        sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
        petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
        petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
        # create data object
        data = {
            'sepal-length': sepal_length,
            'sepal-width': sepal_width,
            'petal-length': petal_length,
            'petal-width': petal_width,
        }
        # create df
        features = pd.DataFrame(data, index=[0])

        return features

    df = sidebar_input()

    st.subheader("User Input")
    st.write(df)

    ## Machine Learning Classificaton

    #get data
    iris = datasets.load_iris()
    X = iris.data
    Y = iris.target

    # create and train clf
    clf = RandomForestClassifier()
    clf.fit(X, Y)

    #prediction of clf with Input data
    prediction= clf.predict(df)
    prediction_proba= clf.predict_proba(df)

    # output of randomforest clf

    st.subheader('Class labels and their corresponding index number')
    st.write(iris.target_names)

    st.subheader('Prediction')
    st.write(iris.target_names[prediction])
    st.write(prediction)
    st.subheader('Prediction Probability')
    st.write(prediction_proba)