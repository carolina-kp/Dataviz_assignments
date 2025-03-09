import streamlit as st
import seaborn as sns
import pandas as pd
import time
import plotly.express as px
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="Diamond Market Analysis", layout="wide")

st.title("Database Design Questions: Diamond Market Analysis")
st.write("Data automatically updates when Google Sheet changes")

csv_url = "https://docs.google.com/spreadsheets/d/1UFaq5QBW6F1ulq38_FTOjRy-qDZQPosi4Zc10SbZG3U/export?format=csv"
diamond_data = pd.read_csv(csv_url, on_bad_lines="skip", encoding="utf-8")
diamond_data["carat"] = pd.to_numeric(diamond_data["carat"], errors="coerce")
diamond_data["price"] = pd.to_numeric(diamond_data["price"], errors="coerce")

if "progress_stage" not in st.session_state:
    st.session_state.progress_stage = 0 
    st.session_state.start_time = None
    st.session_state.answer_time_1 = None   
    st.session_state.answer_time_2 = None
    st.session_state.random_chart = None

if "question_order" not in st.session_state:
    st.session_state.question_order = random.sample([1, 2], 2) 

def show_chart(question_number):
    if question_number == 1:
        st.write("### Question 1: What is the relationship between carat size and price?")
        scatter_chart = px.scatter(
            diamond_data, x="carat", y="price", color="cut",
            title="Diamond Price vs. Carat Size",
            labels={"carat": "Carat Size", "price": "Price ($)"}
        )
        st.plotly_chart(scatter_chart, use_container_width=True)
    elif question_number == 2:
        st.write("### Question 2: How does the number of diamonds vary across different colors?")
        color_counts = diamond_data["color"].value_counts().reset_index()
        color_counts.columns = ["Color", "Count"]
        
        bar_chart = px.bar(
            color_counts, 
            x="Color", 
            y="Count",
            title="Number of Diamonds by Color",
            labels={"Color": "Diamond Color", "Count": "Number of Diamonds"},
            color="Color"
        )
        st.plotly_chart(bar_chart, use_container_width=True)


if st.session_state.progress_stage == 0:
    show_chart(st.session_state.question_order[0])  
    st.session_state.start_time = time.time()
    st.session_state.progress_stage = 1


if st.session_state.progress_stage == 1 and st.button("I answered this question"):
    st.session_state.answer_time_1 = time.time() - st.session_state.start_time
    st.success(f"Time taken to answer: {st.session_state.answer_time_1:.2f} seconds")
    st.session_state.progress_stage = 2
    st.session_state.start_time = time.time() 
    st.session_state.question_order.pop(0)  
    st.rerun() 

if st.session_state.progress_stage == 2:
    show_chart(st.session_state.question_order[0])  

    if st.button("I answered this question too"):
        st.session_state.answer_time_2 = time.time() - st.session_state.start_time
        st.success(f"Time taken to answer: {st.session_state.answer_time_2:.2f} seconds")
        st.session_state.progress_stage = 3  # End of quiz
        st.rerun()
if st.session_state.answer_time_1:
    st.write(f"**Time for first question:** {st.session_state.answer_time_1:.2f} seconds")

if st.session_state.answer_time_2:
    st.write(f"**Time for second question:** {st.session_state.answer_time_2:.2f} seconds")

# Reset button to clear everything and start over
if st.session_state.progress_stage == 3 and st.button("Reset Quiz"):
  
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.progress_stage = 0 
    st.session_state.answer_time_1 = None  
    st.session_state.answer_time_2 = None  
    st.rerun()  
