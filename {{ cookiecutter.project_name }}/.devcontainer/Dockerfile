ARG PYTHON_VERSION
FROM mcr.microsoft.com/vscode/devcontainers/python:$PYTHON_VERSION

ENV DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    ca-certificates \
    git \
    openssh-client \
    # https://forums.docker.com/t/how-can-i-run-docker-command-inside-a-docker-container/337
    docker.io \
    && apt-get autoremove -y \
    && apt-get clean -y

# AWS CLI

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install -i /usr/local/aws-cli -b /usr/local/bin

# Configure poetry and act for local testing of GitHub Actions

USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# Configure AWS command-line completion

RUN echo "complete -C '/usr/local/bin/aws_completer' aws" >> ~/.bashrc