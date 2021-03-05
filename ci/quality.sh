#!/bin/sh

set -e

# Check linters pass
grunt lint

# Check coverage reports are present
echo 'Skip checking coverage reports are present'
