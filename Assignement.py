import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import random
import time
import matplotlib.pyplot as plt
import plotly.express as px

# Load dataset (Seaborn's Diamonds dataset)
df = sns.load_dataset("diamonds").sample(1000)  # Use a sample for performance

# Initialize session state variables
if "chart_selected" not in st.session_state:
    st.session_state.chart_selected = False
    st.session_state.start_time = None
    st.session_state.selected_chart = None
    st.session_state.answer_time_1 = None
    st.session_state.answer_time_2 = None

# App Title
st.title("💎 A/B Testing: Diamond Price Analysis")

# Display the business question
st.write("### ❓ How does the price of diamonds change based on cut quality?")

# Button to randomly select a chart
if st.button("Show Chart"):
    st.session_state.chart_selected = True
    st.session_state.start_time = time.time()  # Start timer
    st.session_state.selected_chart = random.choice(["Chart A", "Chart B"])
    st.rerun()

# Show chart based on random selection
if st.session_state.chart_selected:
    st.write(f"### 📊 {st.session_state.selected_chart}")

    if st.session_state.selected_chart == "Chart A":
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(x="cut", y="price", data=df, ax=ax, palette="Blues")
        ax.set_title("Diamond Prices by Cut Quality")
        st.pyplot(fig)

    else:
        fig = px.scatter(df, x="carat", y="price", color="cut", title="Diamond Price vs. Carat Size")
        st.plotly_chart(fig)

    # Button to record the response time
    if st.button("I answered your question"):
        elapsed_time = time.time() - st.session_state.start_time

        if st.session_state.answer_time_1 is None:
            st.session_state.answer_time_1 = elapsed_time
            st.success(f"✅ Time for question 1: **{elapsed_time:.2f} seconds**")
        elif st.session_state.answer_time_2 is None:
            st.session_state.answer_time_2 = elapsed_time
            st.success(f"✅ Time for question 2: **{elapsed_time:.2f} seconds**")

# Show recorded times
if st.session_state.answer_time_1:
    st.write(f"⏳ **Time for first question:** {st.session_state.answer_time_1:.2f} seconds")

if st.session_state.answer_time_2:
    st.write(f"⏳ **Time for second question:** {st.session_state.answer_time_2:.2f} seconds")
