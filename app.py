import streamlit as st
import requests

API_URL = "https://lds-ai.onrender.com/api/v1/prediction/4fffec95-202e-4fbd-ad00-c8125a879644"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

st.title('LDS Ai Helper Bot')

message = st.text_input('Enter your message')

if st.button('Send'):
    response = query({"question": message})
    st.write(response)
