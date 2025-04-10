import os
from pathlib import Path
import logging
import argparse


# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# CLI argument for project name
parser = argparse.ArgumentParser()
parser.add_argument('--project', default='dlproject', help="Project name")
args = parser.parse_args()
project_name = args.project


# List of files to be created
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    ".github/workflows/.gitkeep"
]

# Optional default content for certain files
default_file_content = {
    "setup.py": f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.0.1",
    author="Ankit Kaswan",
    packages=find_packages(where="src"),
    package_dir={{"": "src"}},
    install_requires=[],
)
"""
}

# Create files and folders
for filepath in list_of_files:
    filepath = Path(os.path.normpath(filepath))
    filedir, filename = os.path.split(filepath)

    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logger.info(f"Creating directory: {filedir} for file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w") as f:
            content = default_file_content.get(str(filepath), "")
            f.write(content)
        logger.info(f"Created file: {filepath}")
    else:
        logger.info(f"File already exists: {filepath}")
