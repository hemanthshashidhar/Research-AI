from langgraph.graph import END
from langgraph.graph import StateGraph

from app.agents.planner import planner_node
from app.graph.state import ResearchState


builder = StateGraph(ResearchState)

builder.add_node(
    "planner",
    planner_node
)

builder.set_entry_point(
    "planner"
)

builder.add_edge(
    "planner",
    END
)

graph = builder.compile()
