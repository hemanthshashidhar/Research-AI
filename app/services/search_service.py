from duckduckgo_search import DDGS


def web_search(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using DuckDuckGo.

    Returns:
        List of dictionaries containing
        title,
        url,
        snippet.
    """

    results = []

    with DDGS() as ddgs:

        response = ddgs.text(
            query,
            max_results=max_results,
        )

        for item in response:

            results.append(
                {
                    "title": item.get("title", ""),
                    "url": item.get("href", ""),
                    "snippet": item.get("body", ""),
                }
            )

    return results
