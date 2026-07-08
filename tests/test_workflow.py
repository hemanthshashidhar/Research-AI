from app.graph.workflow import graph


def test_workflow():

    state = {
        "topic": "Compare LangGraph and CrewAI",
        "planner_output": [],
        "search_results": [],
        "documentation": [],
        "github_analysis": {},
        "review": "",
        "report": "",
    }

    result = graph.invoke(state)

    print()

    print("=" * 60)
    print("Execution Plan")
    print("=" * 60)

    for task in result["planner_output"]:
        print(task)

    print("=" * 60)


if __name__ == "__main__":
    test_workflow()
