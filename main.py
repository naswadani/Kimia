import streamlit as st
from web_function import load_data

from Tabs import predict, visualise, aboutme

Tabs = {
    "Prediction": predict,
    "Visualisation": visualise,
    "About Me"  : aboutme
}

st.sidebar.title("Navigasi")

page = st.sidebar.radio("Pages",list(Tabs.keys()))
df, x, y = load_data()
if page in ["Prediction", "Visualisation"]: 
    Tabs[page].app(df,x,y) 
else:
    Tabs[page].app()