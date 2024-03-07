import subprocess

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

print(get_unmerged_commits())