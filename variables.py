import streamlit as st

if 'my_variable' not in st.session_state:

    st.session_state.myvariable = 5

button =st.button("Click!")

text= f"Variable Before: {st.session_state.myvariable}"


if button:
    st.session_state.myvariable += 1

f"Variable After: {st.session_state.myvariable}"
