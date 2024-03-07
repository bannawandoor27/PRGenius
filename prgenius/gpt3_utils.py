# gpt3_utils.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

def load_openai_api_key():
    """Load the OpenAI API key from an environment variable."""
    return os.getenv('OPENAI_API_KEY')

def generate_pr_description(commits,repo_name,repo_details):
    """Generates a pull request description using GPT-3 based on commit messages."""
    # Load the OpenAI API key
    api_key = load_openai_api_key()
    if not api_key:
        print("OpenAI API key is not set. Please check your .env file or environment variables.")
        return None

    openai.api_key = api_key

    # Join the commits into a single string, each commit on a new line
    commits_str = "\n".join(commits)
    prompt = f"Generate a pull request description in markdown format with a good heading based on these commits:\n{commits_str}"
    project_name = repo_name
    project_summary = repo_details.get('description', 'No description available.')  # Use the repo description

    commits_str = "\n".join([f"- {commit}" for commit in commits])  # Format commits as a list
    prompt = (
        f"Given the following commits to the '{project_name}', which is described as: '{project_summary}',"
        f" create a detailed pull request description. The description should include a title, a summary of changes,"
        f" the impact of these changes on the project, any additional notes for the reviewers, and if applicable,"
        f" warnings about potential breaking changes or areas that need careful review. Please format the description in Markdown.\n\n"
        f"Commits:\n{commits_str}\n"
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Failed to generate PR description: {e}")
        return None
