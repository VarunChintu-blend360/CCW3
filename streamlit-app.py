import streamlit as st

st.title("👋 Hi there!")

# Simple button
if st.button("Click me!"):
    st.write("You clicked the button 🎉")
else:
    st.write("Waiting for you to click...")
