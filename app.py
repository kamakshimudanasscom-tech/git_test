import streamlit as st

st.title("Addition Program")

num1 = st.number_input("first number")
num2 = st.number_input("second number")

if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition = {result}")
