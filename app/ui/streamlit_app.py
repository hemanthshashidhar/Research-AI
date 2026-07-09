import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT))

from app.services.export_service import generate_pdf
import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ResearchOS AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.title("ResearchOS AI")

    st.markdown(
        """
Enterprise Multi-Agent
Research Platform
"""
    )

    st.divider()

    st.subheader("Workflow")

    st.success("Planner")
    st.success("Search")
    st.success("GitHub")
    st.success("Reviewer")
    st.success("Report")

    st.divider()

    st.subheader("Technology")

    st.markdown(
        """
- LangGraph
- LangChain
- FastAPI
- Streamlit
- Gemini
- GitHub API
- DDGS Search
"""
    )

    st.divider()

    st.caption("Version 1.0")

# -----------------------------
# Header
# -----------------------------

st.title("ResearchOS AI")

st.caption(
    "Enterprise Multi-Agent AI Research Platform"
)

st.markdown("---")

# -----------------------------
# Research Input
# -----------------------------

topic = st.text_input(
    "Research Topic",
    placeholder="Example: Compare LangGraph and CrewAI",
)

research_clicked = st.button(
    "Research",
    use_container_width=True,
)

# -----------------------------
# Main Workflow
# -----------------------------

if research_clicked:

    if not topic.strip():

        st.warning("Please enter a research topic.")

        st.stop()

    with st.spinner("Running Multi-Agent Workflow..."):

        response = requests.post(
            f"{API_URL}/research",
            json={
                "topic": topic,
            },
            timeout=300,
        )

    if response.status_code != 200:

        st.error(response.text)

        st.stop()

    data = response.json()

    st.success("Research completed successfully!")

    st.markdown("---")

    # -----------------------------
    # Metrics
    # -----------------------------

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:

        st.metric(
            "Planner",
            "Completed",
        )

    with metric2:

        st.metric(
            "Sources",
            len(data["search_summary"]),
        )

    with metric3:

        repo = data.get("github", {})

        if repo:

            st.metric(
                "Repository",
                "Found",
            )

        else:

            st.metric(
                "Repository",
                "None",
            )

    with metric4:

        st.metric(
            "Report",
            "Ready",
        )

    st.markdown("---")

    # -----------------------------
    # Workflow Status
    # -----------------------------

    st.subheader("Workflow Status")

    c1, c2, c3, c4, c5 = st.columns(5)

    with c1:
        st.success("Planner")

    with c2:
        st.success("Search")

    with c3:
        st.success("GitHub")

    with c4:
        st.success("Reviewer")

    with c5:
        st.success("Report")

    st.markdown("---")

    # -----------------------------
    # Tabs
    # -----------------------------

    plan_tab, github_tab, review_tab, report_tab, source_tab = st.tabs(
        [
            "Execution Plan",
            "GitHub",
            "Reviewer",
            "Report",
            "Sources",
        ]
    )

    # -----------------------------
    # Execution Plan
    # -----------------------------

    with plan_tab:

        st.subheader("Execution Plan")

        for i, step in enumerate(
            data["execution_plan"],
            start=1,
        ):

            st.markdown(
                f"**{i}.** {step}"
            )
         # -----------------------------
    # GitHub Tab
    # -----------------------------

    with github_tab:

        st.subheader("Repository Analysis")

        github = data.get("github", {})

        if github:

            with st.container(border=True):

                col1, col2 = st.columns([3, 1])

                with col1:

                    st.markdown(
                        f"### {github['name']}"
                    )

                    st.write(
                        github["description"]
                    )

                    st.markdown(
                        f"**Language:** {github['language']}"
                    )

                with col2:

                    st.metric(
                        "Stars",
                        github["stars"],
                    )

                st.link_button(
                    "Open Repository",
                    github["url"],
                    use_container_width=True,
                )

        else:

            st.info(
                "No repository found."
            )

    # -----------------------------
    # Reviewer Tab
    # -----------------------------

    with review_tab:

        st.subheader("Reviewer Notes")

        st.markdown(
            data["review"]
        )


        # -----------------------------
    # Report Tab
    # -----------------------------

    with report_tab:

        st.subheader("Final Technical Report")

        st.markdown(data["report"])

        col1, col2 = st.columns(2)

        with col1:

            st.download_button(
                label="Download Report (.md)",
                data=data["report"],
                file_name=f"{topic.replace(' ', '_')}.md",
                mime="text/markdown",
                use_container_width=True,
            )

        with col2:

            pdf = generate_pdf(data["report"])

            st.download_button(
                label="Download Report (.pdf)",
                data=pdf,
                file_name=f"{topic.replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

   
    # -----------------------------
    # Sources Tab
    # -----------------------------

    with source_tab:

        st.subheader(
            "Research Sources"
        )

        for index, source in enumerate(
            data["search_summary"],
            start=1,
        ):

            with st.expander(
                f"{index}. {source['title']}",
                expanded=False,
            ):

                st.write(
                    source["snippet"]
                )

                st.link_button(
                    "Open Source",
                    source["url"],
                    key=f"source_{index}",
                )

    st.markdown("---")

    st.caption(
        "Research completed using the Planner, Search, GitHub, Reviewer and Report Agents."
    )
