# PRGenius

PRGenius automates the creation of pull requests on GitHub by leveraging OpenAI's GPT-3 to generate meaningful and detailed descriptions from your commit messages. It streamlines the PR process, making it easier and more efficient for developers.

## Features

- **Automated PR Descriptions**: Generate detailed PR descriptions from commit messages using GPT-3.
- **Flexible**: Works with any GitHub repository, supporting customizable base and head branches.
- **Easy Integration**: Seamlessly integrates into your development workflow with minimal setup.

## Getting Started

### Prerequisites

- Python 3.7+
- A GitHub account
- An OpenAI API key

### Installation

Install PRGenius using pip:

```bash
pip install prgenius
```

### Configuration

Before using PRGenius, configure your environment with the necessary credentials:

1. **GitHub Token**: Create a GitHub Personal Access Token (PAT) with repository access. Follow the instructions on GitHub to [create a token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

2. **OpenAI API Key**: Obtain an API key by creating an account at [OpenAI](https://openai.com/) and accessing your API keys section.

Set the following environment variables:

```plaintext
GITHUB_REPO_OWNER=<your-github-username>
GITHUB_REPO_NAME=<your-repository-name>
GITHUB_TOKEN=<your-github-token>
OPENAI_API_KEY=<your-openai-api-key>
```

