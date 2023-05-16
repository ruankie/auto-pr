[![GitHub stars](https://img.shields.io/github/stars/ruankie/auto-pr)](https://github.com/ruankie/auto-pr/stargazers)
[![GitHub last commit](https://img.shields.io/github/last-commit/ruankie/auto-pr)](https://github.com/ruankie/auto-pr/commits/main)

# auto-pr

## Description

Automatically generates detailed pull request message suggestions based on commit history. This is done using GPT type large language models (LLMs) through Azure's OpenAI Service and LangChain.

## Setup
1. Set up your virtual env with all the required dependencies
    ```shell
    poetry install
    ```
2. Set your environment variables in a file called `.env` (see `.env.example`)
3. [Create a resource and deploy a model using Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/how-to/create-resource?pivots=web-portal)

## Usage

> Note: Whe using notebooks, make sure you activate the correct poetry environment. You can set your Python kernel to the value that gets returned when you run `poetry run which python`.

1. Browse the example notebooks in `notebooks/`

## Useful Resources
- 