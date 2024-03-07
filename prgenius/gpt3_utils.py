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
        f" create a detailed pull request description of not less than 250 words. The description should be comprehensive and include:"
        f"\n- A title for the pull request,"
        f"\n- A summary of changes explaining the purpose and scope,"
        f"\n- The impact of these changes on the project,"
        f"\n- Any additional notes for the reviewers that might help understand the context or the reason behind the changes,"
        f"\n- Warnings about potential breaking changes or areas that need careful review,"
        f"\n\nPlease ensure the description is well-structured, clear, and formatted in Markdown.\n\n"
        f"Commits:\n{commits_str}\n"
    )
    # Might improvise this later, confused whether to include warnings or not
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
    
def generate_pr_title(commits, repo_name, repo_details):
    """Generates a pull request title using GPT-3 based on commit messages."""
    api_key = load_openai_api_key()
    if not api_key:
        print("OpenAI API key is not set. Please check your .env file or environment variables.")
        return None

    openai.api_key = api_key

    commits_str = "\n".join([f"- {commit}" for commit in commits])
    project_name = repo_name
    project_summary = repo_details.get('description', 'No project description available.')

    prompt = (
        f"Based on the following commits for the project '{project_name}' ({project_summary}), "
        f"generate a concise and informative pull request title that summarizes the main change or feature being introduced. "
        f"The title should give a clear idea of what the change entails at a glance.\n\n"
        f"Commits:\n{commits_str}\n"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,
            max_tokens=60, 
            temperature=0.7, 
            frequency_penalty=0.5,  
            presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Failed to generate PR title: {e}")
        return None


def generate_pr_content(commits, repo_name, repo_details):
    """Generates a pull request title and description using GPT-3 based on commit messages."""
    api_key = load_openai_api_key()
    if not api_key:
        print("OpenAI API key is not set. Please check your .env file or environment variables.")
        return None, None

    openai.api_key = api_key

    commits_str = "\n".join([f"- {commit}" for commit in commits])
    project_name = repo_name
    project_summary = repo_details.get('description', 'No project description available.')

    prompt = (
        f"Based on the following commits for the project '{project_name}' ({project_summary}), "
        f"generate both a concise and informative pull request title and a detailed description. "
        f"The title should summarize the main change or feature being introduced at a glance. "
        f"The description should be not less than 250 words and include:\n"
        f"- A summary of changes explaining the purpose and scope,\n"
        f"- The impact of these changes on the project,\n"
        f"- Any additional notes for the reviewers,\n"
        f"- Warnings about potential breaking changes or areas needing careful review.\n\n"
        f"Format both the title and the description in Markdown.\n\n"
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
        content = response['choices'][0]['message']['content'].strip()
        split_content = content.split("\n", 1)
        pr_title = split_content[0].strip()
        pr_description = split_content[1].strip() if len(split_content) > 1 else ""
        return pr_title, pr_description
    except Exception as e:
        print(f"Failed to generate PR content: {e}")
        return None, None
