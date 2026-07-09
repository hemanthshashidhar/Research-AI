from langgraph.graph import END, StateGraph

from app.agents.github import github_node
from app.agents.planner import planner_node
from app.agents.report import report_node
from app.agents.reviewer import reviewer_node
from app.agents.search import search_node
from app.graph.state import ResearchState

builder = StateGraph(ResearchState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("search", search_node)
builder.add_node("github", github_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("report", report_node)

# Entry
builder.set_entry_point("planner")

# Flow
builder.add_edge("planner", "search")
builder.add_edge("search", "github")
builder.add_edge("github", "reviewer")
builder.add_edge("reviewer", "report")
builder.add_edge("report", END)

graph = builder.compile()
