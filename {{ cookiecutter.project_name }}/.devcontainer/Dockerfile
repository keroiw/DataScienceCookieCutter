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
    && apt-get autoremove -y \
    && apt-get clean -y

USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 -
RUN curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash