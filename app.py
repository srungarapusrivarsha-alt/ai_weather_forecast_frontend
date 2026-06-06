import streamlit as st
import requests

Server_loc= st.secrets["server_url"].rstrip("/")

st.title("🌤 AI Weather Agent")

city = st.text_input(
    "Enter City"
)
question = st.text_input(
    "Ask Your Weather Question"
)
if st.button("ASK"):
    response=requests.post(f"{Server_loc}/get_weather",params={
        "city":city,
        "question":question
    })
    st.success(response.json()["messages"][-1]["content"])