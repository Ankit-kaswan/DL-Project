"""
file_utils.py

Contains utility functions for reading and writing YAML, JSON, and binary files,
along with getting file sizes.
"""

import json
import yaml
import joblib
import os
from pathlib import Path
from typing import Any, Union
from box import ConfigBox
from box.exceptions import BoxValueError
from cnnClassifier import logger


def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Union[str, Path]): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other error occurs during reading.

    Returns:
        ConfigBox: Parsed YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file loaded: {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is empty")
    except Exception as e:
        raise e


def save_json(path: Union[str, Path], data: dict) -> None:
    """
    Saves a dictionary to a JSON file.

    Args:
        path (Union[str, Path]): Path where the JSON will be saved.
        data (dict): Data to be written.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"JSON saved at: {path}")


def load_json(path: Union[str, Path]) -> ConfigBox:
    """
    Loads a JSON file and returns it as a ConfigBox.

    Args:
        path (Union[str, Path]): Path to the JSON file.

    Returns:
        ConfigBox: Parsed JSON content.
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON loaded from: {path}")
    return ConfigBox(content)


def save_bin(data: Any, path: Union[str, Path]) -> None:
    """
    Saves data to a binary file using joblib.

    Args:
        data (Any): The data to be serialized.
        path (Union[str, Path]): Path to the output file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")


def load_bin(path: Union[str, Path]) -> Any:
    """
    Loads binary data from a file using joblib.

    Args:
        path (Union[str, Path]): Path to the binary file.

    Returns:
        Any: Deserialized Python object.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data


def get_size(path: Union[str, Path]) -> str:
    """
    Gets the size of a file in kilobytes.

    Args:
        path (Union[str, Path]): Path to the file.

    Returns:
        str: File size in KB as a human-readable string.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
