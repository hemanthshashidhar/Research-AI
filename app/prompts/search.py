SEARCH_PROMPT = """
You are an AI Research Assistant.

Below are search results collected from the web.

Your task:

- Read every search result.
- Produce a concise technical summary.
- Keep only the important information.
- Ignore advertisements.
- Avoid repeating information.
- Do not invent facts.

Research Topic

{topic}

Search Results

{results}

Return only the summary.
"""
