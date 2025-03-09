import streamlit as st

col1, col2, col3 = st.columns(3)

initial_value = 0

if 'myvariable' not in st.session_state:

    st.session_state.myvariable = initial_value 

if "initial_value" not in st.session_state:
    st.session_state.initial_value = initial_value


more =st.button("Increase")
less =st.button("Decrease")
reset= st.button("Reset")

st.write(f"Initial Value: {initial_value}")
st.write(f"Current Value: {st.session_state.myvariable}")

with col1:
    if more:
        st.session_state.myvariable += 1
        st.rerun()  # Ensures instant update
   

with col2:
    if less:
        st.session_state.myvariable -= 1
        st.rerun()


with col3:
    if reset:
        st.session_state.myvariable = initial_value
        st.rerun()

if st.session_state.myvariable == 10:
    st.success("🎉 You reached Excellence!")