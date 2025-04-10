from setuptools import setup, find_packages

setup(
    name="dlproject",
    version="0.0.1",
    author="Ankit Kaswan",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
