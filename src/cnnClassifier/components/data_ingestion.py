import os
import time
import urllib.request as request
import zipfile
from pathlib import Path

from cnnClassifier import logger
from cnnClassifier.utils.file_utils import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> None:
        """
        Downloads the dataset from the configured URL if not already present.
        Logs execution time and errors.
        """
        try:
            start_time = time.time()
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"Downloaded: {filename} with info: \n{headers}")
            else:
                logger.info(
                    f"File already exists. Size: {get_size(Path(self.config.local_data_file))}"
                )
            logger.info(f"Download step took {time.time() - start_time:.2f} seconds")
        except Exception as e:
            logger.error(f"Failed to download file: {e}")
            raise e

    def extract_zip_file(self) -> None:
        """
        Extracts the downloaded zip file into the configured unzip directory.
        Logs extraction and handles errors.
        """
        try:
            start_time = time.time()
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file to: {unzip_path}")
            logger.info(f"Extraction step took {time.time() - start_time:.2f} seconds")
        except zipfile.BadZipFile as e:
            logger.error(f"Bad zip file: {e}")
            raise e
        except Exception as e:
            logger.error(f"Failed to extract zip file: {e}")
            raise e
