from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState
from app.agents.planner import planner_node

builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)

builder.set_entry_point("planner")

builder.add_edge("planner", END)

graph = builder.compile()
