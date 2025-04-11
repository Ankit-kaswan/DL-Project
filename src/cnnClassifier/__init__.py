"""
logger.py

Advanced logging setup with custom configuration.
"""

import os
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path
from box import ConfigBox
from utils.file_utils import read_yaml


def configure_logger(config: ConfigBox) -> logging.Logger:
    """
    Configures the logger with the provided configuration.

    Args:
        config (ConfigBox): Configuration object containing logging parameters.

    Returns:
        logging.Logger: Configured logger object.
    """
    # Ensure 'log_level' exists in config, else use default level 'INFO'
    log_level_str = config.get("log_level", "INFO").upper()  # Use uppercase to match logging levels
    try:
        log_level = getattr(logging, log_level_str)
    except AttributeError:
        log_level = logging.INFO  # Default to INFO if invalid level is provided

    # Get log format from config, with a default format
    log_format = config.get("log_format", "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]")

    # Create the logger instance
    logger = logging.getLogger(config.get("logger_name", "cnnClassifierLogger"))  # Logger name from config
    logger.setLevel(log_level)

    # Create formatter for log messages
    formatter = logging.Formatter(log_format)

    # Configure Console Logging (enabled or disabled from config)
    if config.get("log_to_console", True):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # Configure File Logging with rotation (enabled or disabled from config)
    if config.get("log_to_file", True):
        # Get log directory and filename from the config
        log_dir = Path(config.get("log_dir", "logs"))
        log_filename = config.get("log_filename", "running_logs.log")
        log_path = log_dir / log_filename

        # Create log directory if it doesn't exist
        os.makedirs(log_dir, exist_ok=True)

        # Log rotation configuration
        rotation = config.get("rotation", {})
        when = rotation.get("when", "midnight")  # Default to "midnight"
        interval = rotation.get("interval", 1)  # Default to 1
        backup_count = rotation.get("backup_count", 7)  # Default to 7 backups

        # Set up the file handler with rotating logs
        file_handler = TimedRotatingFileHandler(
            filename=str(log_path),
            when=when,
            interval=interval,
            backupCount=backup_count,
            encoding="utf-8"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def setup_logger(config_path: Path = Path("config/logging_config.yaml")) -> logging.Logger:
    """
    Set up the logger by reading configuration from a YAML file.

    Args:
        config_path (Path): Path to the logging configuration YAML file.

    Returns:
        logging.Logger: Configured logger object.
    """
    try:
        # Load configuration from YAML file
        config = read_yaml(config_path)  # Read YAML file into ConfigBox
    except Exception as e:
        raise ValueError(f"Failed to load the logging configuration: {e}")

    # Initialize and return the logger based on the loaded configuration
    return configure_logger(config)


# Initialize the logger using the configuration
logger = setup_logger()

# Example log to show it's working
logger.info("Logger initialized successfully.")
