# pr_creator.py
import requests
from dotenv import load_dotenv
import os
from .git_utils import get_current_branch, get_unmerged_commits
from .gpt3_utils import generate_pr_description

# Load environment variables
load_dotenv()

def create_pull_request(repo_owner, repo_name, github_token, base_branch='develop'):
    """Creates a pull request on GitHub using details from the current branch and commits."""
    head_branch = get_current_branch()
    if not head_branch:
        print("Could not determine the current branch. Exiting...")
        return
    
    commits = get_unmerged_commits()
    if commits== ['']:
        print("No unmerged commits found to create a PR. Exiting...")
        return
    print(commits)
    # pr_description = generate_pr_description(commits=commits)
    pr_description = 'testttt'
    if not pr_description:
        print("Failed to generate PR description. Exiting...")
        return

    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'title': f'Pull Request from {head_branch}',
        'body': pr_description,
        'head': head_branch,
        'base': base_branch
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Pull Request created successfully!")
        print(f"PR URL: {response.json().get('html_url')}")
    else:
        print("Failed to create Pull Request:", response.text)

def main():
    # Extract these variables appropriately, e.g., from environment variables or configuration
    repo_owner = os.getenv('GITHUB_REPO_OWNER')
    repo_name = os.getenv('GITHUB_REPO_NAME')
    github_token = os.getenv('GITHUB_TOKEN')

    if not all([repo_owner, repo_name, github_token]):
        print("Repository owner, name, or GitHub token is not set. Check your .env file or environment variables.")
        return

    create_pull_request(repo_owner, repo_name, github_token)

if __name__ == "__main__":
    main()
