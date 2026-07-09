import requests


GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"


def search_repository(topic: str) -> dict:
    """
    Search GitHub repositories related to the topic.
    Returns the most relevant repository.
    """

    response = requests.get(
        GITHUB_SEARCH_URL,
        params={
            "q": topic,
            "sort": "stars",
            "order": "desc",
            "per_page": 1,
        },
        timeout=30,
    )

    response.raise_for_status()

    data = response.json()

    items = data.get("items", [])

    if not items:
        return {}

    repo = items[0]

    return {
        "name": repo["full_name"],
        "description": repo.get("description"),
        "stars": repo["stargazers_count"],
        "language": repo.get("language"),
        "url": repo["html_url"],
    }
