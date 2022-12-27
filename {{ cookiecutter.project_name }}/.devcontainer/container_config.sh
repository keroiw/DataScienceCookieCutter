# Delete .vscode/ is it exists form the previous build

rm -rf .vscode/

# GitHub setup

## See: https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-wsl-resulting-in-many-modified-files
git config --global core.autocrlf input

## See: https://code.visualstudio.com/docs/devcontainers/containers#_sharing-git-credentials-with-your-container
git config --global user.name "${USER_NAME}"
git config --global user.email "${USER_EMAIL}"

# Poetry setup

poetry self update
poetry install --no-interaction

INTERPRETER_PATH="$(poetry env info --path)"
mkdir .vscode
echo '{
    "python.defaultInterpreterPath": '\"${INTERPRETER_PATH}\"'
}' >> .vscode/settings.json

# Initialize repo

git init .

# Install pre-commit hooks

poetry run pre-commit install --install-hooks
