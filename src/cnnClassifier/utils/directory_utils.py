"""
directory_utils.py

Utility for creating directories.
"""

import os
from pathlib import Path
from typing import List, Union
from cnnClassifier import logger


def create_directories(path_to_directories: List[Union[str, Path]], verbose: bool = True) -> None:
    """
    Creates multiple directories if they don't exist.

    Args:
        path_to_directories (List[Union[str, Path]]): List of directory paths to create.
        verbose (bool): If True, logs each creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")
