import subprocess
import requests

def get_current_branch():
    try:
        branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode().strip()
        return branch
    except subprocess.CalledProcessError:
        return None

def get_unmerged_commits(branch='origin/develop'):
    subprocess.check_output(['git', 'fetch', 'origin'])
    merge_base = subprocess.check_output(['git', 'merge-base', 'HEAD', branch]).decode('utf-8').strip()
    commits = subprocess.check_output(['git', 'log', f'{merge_base}..HEAD', '--pretty=format:%s']).decode('utf-8')
    return commits.strip().split('\n')

def push_to_origin(head_branch):
    """Pushes the current branch to the remote origin."""
    try:
        subprocess.check_call(['git', 'push', 'origin', head_branch])
        print(f"Branch {head_branch} pushed to origin successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Failed to push {head_branch} to origin. Error: {e}")
        return False
    
def fetch_repo_details(repo_owner, repo_name, github_token):
    """Fetches repository details from GitHub."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()  # Return the JSON response with repository details
    else:
        print("Failed to fetch repository details:", response.text)
        return {}