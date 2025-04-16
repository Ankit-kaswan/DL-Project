from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.entity.config_entity import PredictionConfig
from cnnClassifier.components.prediction import Prediction
from cnnClassifier import logger

STAGE_NAME = "Prediction stage"


class PredictionPipeline:
    def __init__(self, image_path: str):
        """
        Initializes the PredictionPipeline.
        """
        self.image_path = image_path

    def main(self):
        """
        Main method to run the prediction pipeline.
        """
        # Load the configuration
        config_manager = ConfigurationManager()
        prediction_config = config_manager.get_prediction_config()

        # Initialize Prediction component
        prediction_component = Prediction(prediction_config)

        # Run prediction for the given image (This can be dynamic based on your input)
        result = prediction_component.predict(self.image_path)

        # Log or handle the result as needed (e.g., print to console, save to a file, etc.)
        logger.info(f"Prediction result: {result}")

        return result


if __name__ == '__main__':
    try:
        logger.info("*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

        # Set the image path dynamically or via args/config
        image_path = "path/to/image.jpg"

        # Create the pipeline and run it
        obj = PredictionPipeline(image_path=image_path)
        obj.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
