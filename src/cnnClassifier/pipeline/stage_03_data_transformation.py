from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_transformation import DataTransformation
from cnnClassifier import logger


STAGE_NAME = "Data Transformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        train_gen, test_gen = data_transformation.get_data_generators()


if __name__ == '__main__':
    try:
        logger.info(f"\n\n>>>>>>>> Stage: {STAGE_NAME} started <<<<<<<<")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f">>>>>>>> Stage: {STAGE_NAME} completed successfully <<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(f"Exception in {STAGE_NAME}: {e}")
        raise e
