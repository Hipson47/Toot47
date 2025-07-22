#!/bin/bash
echo "Installing pre-commit hooks..."
pip install pre-commit
pre-commit install
echo "pre-commit hooks installed successfully." 