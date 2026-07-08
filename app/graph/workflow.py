from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState


def start_node(state: ResearchState):

    print("Workflow Started")

    return state


builder = StateGraph(ResearchState)

builder.add_node("start", start_node)

builder.set_entry_point("start")

builder.add_edge("start", END)

graph = builder.compile()
