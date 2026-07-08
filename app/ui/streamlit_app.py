import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ResearchOS AI",
    layout="wide",
)

st.title("ResearchOS AI")

st.caption("Enterprise Multi-Agent AI Research Platform")

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Compare LangGraph and CrewAI",
)

if st.button("Research", use_container_width=True):

    if not topic.strip():
        st.warning("Enter a research topic.")
        st.stop()

    with st.spinner("Planner Agent is generating the execution plan..."):

        response = requests.post(
            f"{API_URL}/research",
            json={
                "topic": topic
            },
            timeout=120,
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    data = response.json()

    st.success("Execution plan generated")

    st.subheader("Execution Plan")

    for index, task in enumerate(
        data["execution_plan"],
        start=1,
    ):
        st.markdown(f"**{index}.** {task}")
