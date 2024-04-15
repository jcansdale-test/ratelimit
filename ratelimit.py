import requests
import json
import os

GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Define the GraphQL query
query = """
{
  repository(owner:"octocat", name:"Hello-World") {
    name
    description
  }
}
"""

# Define the headers
headers = {
    "Authorization": "Bearer " + GITHUB_TOKEN,
    "Content-Type": "application/json"
}

# Make the request
response = requests.post('https://api.github.com/graphql', headers=headers, data=json.dumps({"query": query}))

# Print the RateLimit headers
for key, value in response.headers.items():
    if key.startswith("X-RateLimit-"):
        print(f"{key}: {value}")
