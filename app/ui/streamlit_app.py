import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ResearchOS AI",
    page_icon="🔬",
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
        st.warning("Please enter a research topic.")
        st.stop()

    try:
        with st.spinner("Researching..."):

            response = requests.post(
                f"{API_URL}/research",
                json={"topic": topic},
                timeout=120,
            )

        if response.status_code != 200:
            st.error(f"Backend Error ({response.status_code})")
            st.code(response.text)
            st.stop()

        data = response.json()

        # -------------------------------
        # Execution Plan
        # -------------------------------

        st.success("Research plan generated successfully!")

        st.subheader("Execution Plan")

        execution_plan = data.get("execution_plan", [])

        if execution_plan:
            for index, step in enumerate(execution_plan, start=1):
                st.markdown(f"**{index}.** {step}")
        else:
            st.info("No execution plan returned.")

        # -------------------------------
        # Search Summary
        # -------------------------------

        st.divider()

        st.subheader("Search Summary")

        search_summary = data.get("search_summary", [])

        if search_summary:
            for summary in search_summary:
                st.write(summary)
        else:
            st.info("Search Agent has not returned any summary yet.")

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to the FastAPI backend.\n\n"
            "Make sure Uvicorn is running:\n\n"
            "uvicorn app.main:app --reload"
        )

    except Exception as e:
        st.exception(e)
