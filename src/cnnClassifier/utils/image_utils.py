"""
image_utils.py

Contains functions to encode and decode images using base64.
"""

import base64


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
