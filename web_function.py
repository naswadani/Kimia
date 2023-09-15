import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
import streamlit as st

@st.cache_data()
def load_data():
    df = pd.read_csv('kimia_data.csv')
    x =df[["Semester1","Semester2","Semester3","Semester4","Semester5"]]
    y =df[['Target']]

    return df,x,y

@st.cache_data()
def train_model(x,y):
    model = DecisionTreeClassifier(criterion="entropy", max_depth=3)
    # Train
    model.fit(x,y)
    score = model.score(x,y)
    return model,score
    

#Predict

def predict(x,y,features):
    model, score = train_model(x,y)
    prediction = model.predict(np.array(features).reshape(1,-1))
    return prediction, score