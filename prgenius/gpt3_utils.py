# gpt3_utils.py
import openai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

def load_openai_api_key():
    """Load the OpenAI API key from an environment variable."""
    return os.getenv('OPENAI_API_KEY')

def generate_pr_description(commits):
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
