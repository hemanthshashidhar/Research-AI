from google import genai

from app.config import GEMINI_API_KEY
from app.graph.state import ResearchState

client = genai.Client(api_key=GEMINI_API_KEY)


def planner_node(state: ResearchState):

    prompt = f"""
You are an AI Research Planner.

Your job is NOT to answer the question.

Break the research topic into a short list of research tasks.

Topic:

{state["topic"]}

Return only a numbered list.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    plan = response.text

    state["planner_output"] = plan.split("\n")

    return state
