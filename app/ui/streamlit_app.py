import requests
import streamlit as st

st.set_page_config(
    page_title="ResearchOS AI",
    page_icon="🔬",
    layout="wide"
)

st.title("ResearchOS AI")

st.write("Enterprise Multi-Agent AI Research Platform")

if st.button("Check Backend"):

    response = requests.get("http://127.0.0.1:8000/health")

    if response.status_code == 200:
        st.success(response.json()["status"])
    else:
        st.error("Backend Offline")
