from langgraph.graph import StateGraph, END

from app.graph.state import ResearchState

from app.agents.planner import planner_node
from app.agents.search import search_node
from app.agents.github import github_node
from app.agents.reviewer import reviewer_node


builder = StateGraph(ResearchState)

# -------------------------
# Nodes
# -------------------------

builder.add_node("planner", planner_node)
builder.add_node("search", search_node)
builder.add_node("github", github_node)
builder.add_node("reviewer", reviewer_node)

# -------------------------
# Entry Point
# -------------------------

builder.set_entry_point("planner")

# -------------------------
# Workflow
# -------------------------

builder.add_edge("planner", "search")
builder.add_edge("search", "github")
builder.add_edge("github", "reviewer")
builder.add_edge("reviewer", END)

# -------------------------
# Compile
# -------------------------

graph = builder.compile()
