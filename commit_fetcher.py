import subprocess

def get_unmerged_commits(branch='main'):
    """Fetches commit messages from the current branch that are not in the main branch."""
    commits = subprocess.check_output(['git', 'log', f'{branch}..HEAD', '--pretty=format:%s']).decode('utf-8')
    return commits.strip().split('\n')
