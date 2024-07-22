#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Install pip if not already installed
if ! command -v pip &> /dev/null; then
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py --user
    export PATH="$HOME/.local/bin:$PATH"
fi

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput
