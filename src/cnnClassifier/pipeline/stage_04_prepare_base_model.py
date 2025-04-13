from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel
from cnnClassifier import logger


STAGE_NAME = "Prepare base model"


class PrepareBaseModelTrainingPipeline:
    """
    This pipeline stage handles downloading or loading the base model (e.g., VGG16),
    applies optional layer freezing, and compiles a full classification model
    with the given configurations.
    """

    def __init__(self):
        logger.info(f"{STAGE_NAME} pipeline initialized")

    def main(self):
        logger.info("Fetching configuration for base model preparation")
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()

        logger.info("Creating base model component")
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)

        logger.info("Getting base model from tf.keras.applications")
        prepare_base_model.get_base_model()

        logger.info("Updating base model to full model with custom classification head")
        prepare_base_model.update_base_model()


if __name__ == '__main__':
    try:
        logger.info("*******************")
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
