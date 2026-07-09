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

    with st.spinner("Running multi-agent workflow..."):

        response = requests.post(
            f"{API_URL}/research",
            json={"topic": topic},
            timeout=120,
        )

    if response.status_code != 200:
        st.error(response.text)
        st.stop()

    data = response.json()

    st.success("Research completed")

    st.subheader("Execution Plan")

    for index, task in enumerate(data["execution_plan"], start=1):
        st.markdown(f"**{index}.** {task}")

    st.divider()

    st.subheader("Search Summary")

    for summary in data["search_summary"]:
        st.write(summary)

    st.divider()

    st.subheader("GitHub Repository")

    github = data.get("github", {})

    if github:
        st.markdown(f"**Repository:** {github['name']}")
        st.markdown(f"**Description:** {github['description']}")
        st.markdown(f"**Language:** {github['language']}")
        st.markdown(f"**Stars:** ⭐ {github['stars']}")
        st.markdown(f"**URL:** {github['url']}")
    else:
        st.info("No matching repository found.")
