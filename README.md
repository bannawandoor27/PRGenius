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

You can optionally specify base branch in here as 

```plaintext
GITHUB_REPO_BASE_BRANCH=<your-default-branch-in-github>

```
By default GITHUB_REPO_BASE_BRANCH will be 'develop'

These can be set in a `.env` file in the root of your project or exported in your shell session.

### Usage

After setting up your environment, PRGenius can be used to automatically create pull requests with rich, AI-generated descriptions based on your commit messages. 

To use PRGenius, navigate to your project directory and run:

```bash
prgenius create
```

This command will create a new pull request on GitHub using the commits that are on your current branch but not on your base branch (default `develop`).

#### Advanced Usage

For workflows requiring an immediate merge after creating the pull request, PRGenius offers an auto-merge feature. To create and attempt to auto-merge a pull request, use:

```bash
prgenius createmerge
```

This command attempts to merge the newly created pull request if the predefined conditions are met (e.g., passing all status checks). Ensure your GitHub token has sufficient permissions to merge pull requests in the repository.

**Note:** The effectiveness of the auto-merge feature depends on your repository's settings and the permissions associated with your GitHub token. It's recommended to review and configure branch protection rules and merge options accordingly.

## Contributing

We welcome contributions to PRGenius! If you have suggestions for improvements or encounter a bug, please feel free to contribute. Here's how:

1. Fork the project repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -am 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request for review.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details on our code of conduct and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. This means you are free to use, modify, and distribute the project as you see fit, as long as you include the original copyright and permission notice in any copies or substantial portions of the software.

## Acknowledgments

- Thanks to OpenAI for providing the GPT-3 API, enabling the automation of rich text generation.
- Appreciation goes to GitHub for their robust platform and APIs that facilitate software development and collaboration.
- A shoutout to all the developers and contributors who invest their time and effort into open source projects, making tools like PRGenius possible.

For more detailed information on advanced configurations, features, and usage examples, please refer to the [official documentation](https://github.com/bannawandoor27/PRGenius).

Remember, PRGenius is designed to make your development workflow more efficient and automated. We hope it helps you streamline your PR process and focus more on development.
