import streamlit as st
import requests

API_URL = "https://lds-ai.onrender.com/api/v1/prediction/4f13ac2f-d3f9-4114-8e54-e036fb321212"

def query(payload):
    response = requests.post(API_URL, json=payload)
    return response.json()

st.title('LDS Therapist')

message = st.text_input('Enter your message')

if st.button('Send'):
    response = query({"question": message})
    st.write(response)
