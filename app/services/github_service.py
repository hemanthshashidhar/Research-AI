import re
import requests

GITHUB_SEARCH_URL = "https://api.github.com/search/repositories"
GITHUB_REPO_URL = "https://api.github.com/repos"


def extract_repo_from_search_results(search_results: list[dict]) -> str | None:
    """
    Extract the first GitHub repository URL found
    in the search results.
    """

    for result in search_results:

        url = result.get("url", "")

        if "github.com/" not in url:
            continue

        match = re.search(
            r"github\.com/([^/]+)/([^/?#]+)",
            url,
        )

        if match:
            owner = match.group(1)
            repo = match.group(2)

            return f"{owner}/{repo}"

    return None


def get_repository(owner_repo: str) -> dict:

    response = requests.get(
        f"{GITHUB_REPO_URL}/{owner_repo}",
        timeout=30,
    )

    response.raise_for_status()

    repo = response.json()

    return {
        "name": repo["full_name"],
        "description": repo["description"],
        "stars": repo["stargazers_count"],
        "language": repo["language"],
        "url": repo["html_url"],
    }


def search_repository(topic: str) -> dict:

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

    items = response.json().get("items", [])

    if not items:
        return {}

    repo = items[0]

    return {
        "name": repo["full_name"],
        "description": repo["description"],
        "stars": repo["stargazers_count"],
        "language": repo["language"],
        "url": repo["html_url"],
    }
