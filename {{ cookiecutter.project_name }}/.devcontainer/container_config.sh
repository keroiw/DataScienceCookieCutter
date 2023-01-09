#!/bin/bash

# GitHub setup

## See: https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-wsl-resulting-in-many-modified-files
git config --global core.autocrlf input

## See: https://stackoverflow.com/questions/5834014/lf-will-be-replaced-by-crlf-in-git-what-is-that-and-is-it-important
git config --global core.safecrlf false

## See: https://code.visualstudio.com/docs/devcontainers/containers#_sharing-git-credentials-with-your-container
git config --global user.name "{{ cookiecutter.github_name }}"
git config --global user.email "{{ cookiecutter.github_email }}"

# Poetry setup

poetry self update
poetry install --no-interaction

INTERPRETER_PATH="$(poetry env info --path)"
echo '{
    "python.defaultInterpreterPath": '\"${INTERPRETER_PATH}\"'
}' >> .vscode/settings.json

# Initialize repo

DIR=.git
if [ -d "$DIR" ];
then
    echo "$DIR already exists."
else
    git init .
fi

# Install pre-commit hooks

poetry run pre-commit install --install-hooks
