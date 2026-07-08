import requests
import streamlit as st

st.set_page_config(
    page_title="ResearchOS AI",
    layout="wide"
)

st.title("ResearchOS AI")

topic = st.text_input("Research Topic")

if st.button("Research"):

    response = requests.post(
        "http://127.0.0.1:8000/research",
        json={"topic": topic},
    )

    st.subheader("Execution Plan")

    for step in response.json()["planner_output"]:
        st.write(step)
