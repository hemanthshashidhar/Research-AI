from app.services.search_service import web_search

results = web_search("Machine Learning")

print(f"Found {len(results)} results\n")

for index, result in enumerate(results, start=1):
    print("=" * 60)
    print(f"Result {index}")
    print("=" * 60)
    print(result)
