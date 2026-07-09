from app.graph.state import ResearchState

from app.prompts.documentation import DOCUMENTATION_PROMPT

from app.services.llm_service import get_llm

llm = get_llm()


def documentation_node(
    state: ResearchState,
):

    text = ""

    for item in state["search_results"]:

        text += f"""

Title

{item["title"]}

Snippet

{item["snippet"]}

"""

    prompt = DOCUMENTATION_PROMPT.format(
        results=text
    )

    response = llm.invoke(prompt)

    state["documentation"] = [
        response.content
    ]

    return state
