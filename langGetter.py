import requests
import pandas as pd

# Load dataset
df = pd.read_csv("filter_repos.csv")

import requests

GITHUB_TOKEN = "" # need a token to work

def get_github_language(repo_name):
    url = f"https://api.github.com/repos/{repo_name}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {GITHUB_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get("language", "Unknown")
    elif response.status_code == 403:
        print("Rate limit exceeded or permission issue. Try again later.")
    else:
        print(f"Error {response.status_code}: [Repo: {repo_name}]{response.text}")
    
    return "Unknown"


# Add language information to dataset
df["language"] = df["repo_name"].apply(get_github_language)

# Save updated dataset
df.to_csv("filter_repos_with_language.csv", index=False)
print("Updated dataset saved with programming languages.")
