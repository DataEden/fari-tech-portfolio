#!/bin/bash
# This script sets up the environment for the audit dashboard ETL project.

echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete. Run 'python audit_etl.py' to begin processing."
