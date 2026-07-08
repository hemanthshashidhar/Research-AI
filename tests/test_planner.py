from app.graph.workflow import graph


def main():
    result = graph.invoke(
        {
            "topic": "Compare LangGraph and CrewAI",
            "planner_output": [],
            "search_results": [],
            "documentation": [],
            "github_analysis": {},
            "review": "",
            "report": "",
        }
    )

    print("\nExecution Plan:\n")

    for step in result["planner_output"]:
        print(f"- {step}")


if __name__ == "__main__":
    main()
