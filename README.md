# Cookiecutter for kedro-based projects

## Purpose

This repository aims to provide an utility to easily create kedro projects that are integrated with poetry.

Kedro itself doesn't provide starter that would support poetry. The solution is based on the [following discussion](https://github.com/kedro-org/kedro/issues/1722#issuecomment-1195178428).

## Usage

In order to leverage the template one can proceed as follows:

1. Clone the repository
2. Create local virtual environment (instruction assumes Linux OS) and install cookiecutter:
    * ```sudo apt-get install python3-pip```
    * ```sudo pip3 install virtualenv```
    * ```python3 -m venv <path to your venv>```
    * ```source <path to your venv>/bin/activate```
    * ```pip install cookiecutter```
3. Execute: ```cookiecutter <path to cloned repository>``` and provide relevant data
4. Rename ```env.example``` to ```.env```
5. Rename ```cong/local/globals.example.yml``` to ```cong/local/globals.yml```
6. Add ```conf/local/credentials.yml``` and ```cong/local/globals.yml``` to ```.gitignore```.

## Notes

This section summarizes observations gathered during development.

* There's no point of templating github credentials because they will be supplied by each user that is working on the project (the user has to clone the repository and then provide these).
