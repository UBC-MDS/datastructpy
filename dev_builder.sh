#!/bin/bash

# Step 1: Ensure conda is available
if ! command -v conda &> /dev/null
then
    echo "Conda could not be found. Please install Miniconda or Anaconda."
    exit 1
fi

# Step 2: Extract environment name correctly (remove extra quotes)
env_name=$(grep "^name:" environment.yml | awk '{print $2}' | tr -d '"')

if [ -z "$env_name" ]; then
    echo "Error: Could not determine the environment name from environment.yml."
    exit 1
fi

echo "Checking if the environment '$env_name' exists..."
if conda info --envs | awk '{print $1}' | grep -qx "$env_name"; then
    echo "Environment '$env_name' already exists. Skipping creation."
else
    echo "Creating the Conda environment: $env_name"
    conda env create -f environment.yml
fi

# Step 3: Ensure Conda is properly initialized
eval "$(conda shell.bash hook)"

# Step 4: Install dependencies using Poetry
echo "Installing dependencies with Poetry..."
if ! command -v poetry &> /dev/null
then
    echo "Poetry is not installed. Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="$HOME/.local/bin:$PATH"
fi

poetry install

# Step 5: Confirm successful setup
echo "Setup complete! To activate your environment, run:"
echo "    conda activate $env_name"