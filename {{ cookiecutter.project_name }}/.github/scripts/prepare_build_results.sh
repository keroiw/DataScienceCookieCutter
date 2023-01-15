#!/bin/bash

BUILD_FOLDER_NAME="${GITHUB_HEAD_REF}_build"
mkdir $BUILD_FOLDER_NAME $BUILD_FOLDER_NAME/conf
cp -r dist $BUILD_FOLDER_NAME
cp -r conf/base $BUILD_FOLDER_NAME/conf
cp -r conf/local $BUILD_FOLDER_NAME/conf
echo "build_folder_name=${BUILD_FOLDER_NAME}" >> $GITHUB_OUTPUT
echo "destination_folder_name=artifacts/{{ cookiecutter.step_name }}/${GITHUB_ACTOR}/${GITHUB_HEAD_REF}" >> $GITHUB_OUTPUT
