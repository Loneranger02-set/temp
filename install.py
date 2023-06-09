'''#!/usr/bin/env bash
# run build
echo "Info: Using node version: `node -v` and npm version: `npm -v` and yarn version: `yarn -v`"
set -e
SERVICE_DIR='packages/web'

cd $WORKSPACE
rm -rf .npmrc
cd $WORKSPACE/$SERVICE_DIR
time yarn install'''
print("Hello there")
