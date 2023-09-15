import warnings
from sklearn import tree
import streamlit as st

from web_function import train_model

def app(df,x,y):
    st.title("Visualisasi Model")
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse',False)
    if st.checkbox("Plot Decision Tree"):
        model, score = train_model(x,y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth= 3, out_file=None, filled=True, rounded= True,
            feature_names=x.columns, class_names=['nockd','ckd']
        )
        st.graphviz_chart(dot_data)
