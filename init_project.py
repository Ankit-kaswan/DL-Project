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


def create_default_file_content():
    """Creates and returns the default file content for necessary files."""
    return {
        "setup.py": """import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"

REPO_NAME = "DL-Project"
AUTHOR_USER_NAME = "Ankit-kaswan"
SRC_REPO = "DL-Project"
AUTHOR_EMAIL = "ankit.iitd2014@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={{
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    }},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[],  # Add your dependencies here
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
""",
        "README.md": "# DL Project\n\nThis is a boilerplate deep learning project using CNN architecture.\n",
    }


def create_project_structure(project_name: str):
    """Creates the project directory structure and files."""
    # Get the default file content
    default_file_content = create_default_file_content()

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
        "README.md",
        ".gitignore",
        "research/trials.ipynb",
        "templates/index.html",
        ".github/workflows/.gitkeep"
    ]

    # Create directories and files
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

    logger.info("✅ Project structure created successfully!")


def main():
    """Main function to parse arguments and create the project structure."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--project', default='dlproject', help="Project name")
    args = parser.parse_args()
    create_project_structure(args.project)


if __name__ == "__main__":
    main()
