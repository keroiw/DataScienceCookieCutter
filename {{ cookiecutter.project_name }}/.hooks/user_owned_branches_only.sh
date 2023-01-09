#!/bin/bash

branch="$(git rev-parse --abbrev-ref HEAD)"

while getopts ":u:" o; do
    case "${o}" in
        u)
            USER=${OPTARG}
            ;;
    esac
done

if [[ $branch != ${USER}* ]]; then
    echo "Your branch has to start with ${USER}"
    exit 1
fi
