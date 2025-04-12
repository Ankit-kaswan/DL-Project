from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger


STAGE_NAME = "Data Ingestion Stage"


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()

        logger.info("Initializing DataIngestion component...")
        data_ingestion = DataIngestion(config=data_ingestion_config)

        logger.info("Starting download...")
        data_ingestion.download_file()

        logger.info("Starting extraction...")
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} completed successfully <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Exception occurred in {STAGE_NAME}: {e}")
        raise e
