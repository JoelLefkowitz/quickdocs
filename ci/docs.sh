#!/bin/sh

set -e

# Docs are hosteed on readthedocs which uses sphinx-build
# We have a grunt task that can check that sphinx-build passes
grunt docs:build
