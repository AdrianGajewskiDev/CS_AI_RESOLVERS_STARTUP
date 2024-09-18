#! /bin/bash

rm -r build
pip install poetry

poetry install --no-dev
mkdir build && cd build
cp -r $(poetry env info -p)/lib/*/site-packages/* .
cp -r ../resolvers_startup .
zip -r ../cr-ai-resolvers-startup-dev.zip .