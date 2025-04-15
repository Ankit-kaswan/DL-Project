"""
image_utils.py

Contains functions to encode and decode images using base64,
as well as loading and preprocessing images for models.
"""

import base64
import numpy as np
from tensorflow.keras.preprocessing import image


def decode_image(img_string: str, file_name: str) -> None:
    """
    Decodes a base64 string and saves it as an image file.

    Args:
        img_string (str): Base64 encoded image string.
        file_name (str): Destination file name for the image.
    """
    imgdata = base64.b64decode(img_string)
    with open(file_name, 'wb') as f:
        f.write(imgdata)


def encode_image_to_base64(cropped_image_path: str) -> bytes:
    """
    Encodes an image file to base64 bytes.

    Args:
        cropped_image_path (str): Path to the image file.

    Returns:
        bytes: Base64-encoded image content.
    """
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())


def load_image_from_path(image_path: str, target_size=(224, 224), color_mode="rgb") -> np.ndarray:
    """
    Load and preprocess an image from a given file path.

    Args:
        image_path (str): Path to the image.
        target_size (tuple): Desired image size, e.g., (224, 224).
        color_mode (str): Color mode to load the image ('rgb', 'grayscale').

    Returns:
        np.ndarray: Preprocessed image ready for model input.
    """
    img = image.load_img(image_path, target_size=target_size, color_mode=color_mode)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array
