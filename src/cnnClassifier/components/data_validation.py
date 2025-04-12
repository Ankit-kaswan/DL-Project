import os
from cnnClassifier.entity.config_entity import DataValidationConfig
from cnnClassifier import logger


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        logger.info("Starting data validation...")

        all_files = os.listdir(self.config.unzip_dir)
        logger.info(f"Files found: {all_files}")

        validation_status = True
        for file in self.config.required_files:
            if file not in all_files:
                validation_status = False
                logger.warning(f"Required file not found: {file}")
                break

        if validation_status:
            logger.info("All required files are present.")
        else:
            logger.error("Data validation failed. Required files missing.")

        return validation_status
