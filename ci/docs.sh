#!/bin/sh

set -e

# Docs are hosteed on readthedocsw which uses sphinx-build
# We need to check that sphinx-build passes
sphinx-build docs build
