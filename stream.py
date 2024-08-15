import streamlit as st
st.title("Hello streamlit")
st.header("Learning Streamlit")
name = st.text_input(" Enter your name")
feedback = st.text_area("Enter your feedback")
if st.button("Submit"):
    st.write("Thanks for your feedback!")
