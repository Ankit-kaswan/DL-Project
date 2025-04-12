from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_validation import DataValidation
from cnnClassifier import logger


STAGE_NAME = "Data Validation Stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()

        logger.info("Initializing DataValidation component...")
        data_validation = DataValidation(config=data_validation_config)
        validation_status = data_validation.validate_all_files_exist()

        if not validation_status:
            raise Exception("Data validation failed! Missing required files.")


if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
        pipeline = DataValidationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} completed successfully <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
        raise e
