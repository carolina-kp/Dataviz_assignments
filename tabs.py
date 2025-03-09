

import streamlit as st
import seaborn as sns   
import numpy as np


tab1, tab2 = st.tabs(["Home", "About"])


with tab1:
    st.subheader("Home")
    iris = sns.load_dataset("iris")
    chart =sns.barplot(x=species, y=sepal_length , data=iris)
    st.pyplot(chart)

with tab2:
    st.subheader("About")
    st.write("This is a simple example of a Streamlit app with tabs.")