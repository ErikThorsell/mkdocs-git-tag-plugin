#!/bin/bash -xe
poetry run black src/
poetry run flake8 src/