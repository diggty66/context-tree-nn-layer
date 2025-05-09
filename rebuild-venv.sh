#!/bin/bash

echo "Deactivating venv if active..."
deactivate 2>/dev/null

echo "Removing old venv..."
rm -rf venv

echo "Creating new virtual environment..."
python -m venv venv

echo "Activating new venv..."
source venv/Scripts/activate

echo "Upgrading pip, setuptools, wheel..."
python -m pip install --upgrade pip setuptools wheel

echo "✅ Virtual environment rebuilt and ready."
