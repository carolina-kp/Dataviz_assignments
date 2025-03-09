import streamlit as st
import seaborn as sns
import pandas as pd
import random
import time
import matplotlib.pyplot as plt
import plotly.express as px


diamond_data = sns.load_dataset("diamonds").sample(1000) 


if "progress_stage" not in st.session_state:
    st.session_state.progress_stage = 0  # 0: No chart, 1: First chart, 2: Second chart
    st.session_state.start_time = None
    st.session_state.answer_time_1 = None
    st.session_state.answer_time_2 = None


st.title("💎 Database Design Questions: Diamond Market Analysis")

#  Show First Chart Button
st.write("### Question 1: What is the relationship between carat size and price?")

if st.session_state.progress_stage == 0 and st.button("Show First Chart"):
    st.session_state.progress_stage = 1
    st.session_state.start_time = time.time()  # Start tracking time
    st.rerun()

#  First Chart (Carat vs. Price)
if st.session_state.progress_stage >= 1:
    st.write("### Chart 1: Carat Size vs. Price")

    # Scatter Plot (Carat vs. Price)
    scatter_chart = px.scatter(diamond_data, x="carat", y="price", color="cut", 
                               title="Diamond Price vs. Carat Size", labels={"carat": "Carat Size", "price": "Price ($)"})
    st.plotly_chart(scatter_chart)

    # Button to record response time for first question
    if st.session_state.answer_time_1 is None and st.button("I answered this question"):
        st.session_state.answer_time_1 = time.time() - st.session_state.start_time
        st.success(f"Time for question 1: **{st.session_state.answer_time_1:.2f} seconds**")
        st.session_state.progress_stage = 2  # Move to second chart stage
        st.session_state.start_time = time.time()  # Reset timer for next question
        st.rerun()

# Show Second Chart Button
st.write("### Question 2: How does the number of diamonds vary across different colors?")

if st.session_state.progress_stage == 2 and st.button("Show Second Chart"):
    st.session_state.progress_stage = 3
    st.rerun()

# Second Chart (Number of Diamonds per Color)
if st.session_state.progress_stage >= 3:
    st.write("### Chart 2: Number of Diamonds per Color")

    color_counts = diamond_data["color"].value_counts().reset_index()
    color_counts.columns = ["Color", "Count"]

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x="Color", y="Count", data=color_counts, ax=ax, palette= "Set2" )
    ax.set_title("Number of Diamonds by Color")
    ax.set_ylabel("Count of Diamonds")
    st.pyplot(fig)

    if st.session_state.answer_time_2 is None and st.button("I answered this question too"):
        st.session_state.answer_time_2 = time.time() - st.session_state.start_time
        st.success(f"Time for question 2: **{st.session_state.answer_time_2:.2f} seconds**")
        st.session_state.progress_stage = 4  
        st.rerun()

if st.session_state.answer_time_1:
    st.write(f"**Time for first question:** {st.session_state.answer_time_1:.2f} seconds")

if st.session_state.answer_time_2:
    st.write(f"**Time for second question:** {st.session_state.answer_time_2:.2f} seconds")
