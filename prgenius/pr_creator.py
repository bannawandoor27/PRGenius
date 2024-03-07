# pr_creator.py
import argparse
import requests
from dotenv import load_dotenv
import os
from .git_utils import get_current_branch, get_unmerged_commits, push_to_origin,fetch_repo_details
from .gpt3_utils import generate_pr_description

# Load environment variables
load_dotenv()

def create_and_merge_pull_request(repo_owner, repo_name, github_token, head_branch, base_branch, pr_number):
    """
    Attempts to auto-merge the created pull request.
    This is a simplified example and might need adjustments based on merge requirements.
    """
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pr_number}/merge'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {'merge_method': 'merge'}  # Can be 'merge', 'squash', or 'rebase'
    response = requests.put(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Pull Request merged successfully!")
    else:
        print("Failed to merge Pull Request:", response.text)

def create_pull_request(repo_owner, repo_name, github_token, head_branch, base_branch='develop'):
    """Creates a pull request on GitHub using details from the current branch and commits."""
    if not head_branch:
        print("Could not determine the current branch. Exiting...")
        return
    # Ensure the branch is pushed to origin before creating PR
    if not push_to_origin(head_branch):
        print("Exiting due to failure pushing branch to origin.")
        return
    
    commits = get_unmerged_commits()
    if commits == ['']:
        print("No unmerged commits found to create a PR. Exiting...")
        return
    repo_details = fetch_repo_details(repo_owner, repo_name, github_token)
    print("Commits to be included in the PR:", commits)
    pr_description = generate_pr_description(commits=commits,repo_name=repo_name,repo_details=repo_details)
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
        pr_number = response.json().get('number')
        print(f"Pull Request created successfully! PR Number: {pr_number}")
        return pr_number
    else:
        print("Failed to create Pull Request:", response.text)
        return None

        

def main():
    # Extract these variables appropriately, e.g., from environment variables or configuration
    repo_owner = os.getenv('GITHUB_REPO_OWNER')
    repo_name = os.getenv('GITHUB_REPO_NAME')
    github_token = os.getenv('GITHUB_TOKEN')

    if not all([repo_owner, repo_name, github_token]):
        print("Repository owner, name, or GitHub token is not set. Check your .env file or environment variables.")
        return
    # Use environment variable for base branch if not provided as a command-line argument
    base_branch = os.getenv('GITHUB_REPO_BASE_BRANCH', 'develop')

    head_branch = get_current_branch()
    if head_branch is None:
        print("Error determining current branch. Exiting...")
        return
    parser = argparse.ArgumentParser(description='Create and optionally merge a pull request on GitHub.')
    parser.add_argument('action', choices=['create', 'createmerge'], help='Action to perform: create a PR or create and merge a PR.')
    # Other argument definitions remain the same

    args = parser.parse_args()

    # Extracting and checking other necessary variables remain the same

    if args.action == 'createmerge':
        # Create PR and then attempt to merge it
        pr_number = create_pull_request(repo_owner, repo_name, github_token, head_branch, base_branch)
        if pr_number:
            create_and_merge_pull_request(repo_owner, repo_name, github_token, head_branch, base_branch, pr_number)
    else:
        # Just create PR
        create_pull_request(repo_owner, repo_name, github_token, head_branch, base_branch)


if __name__ == "__main__":
    main()
