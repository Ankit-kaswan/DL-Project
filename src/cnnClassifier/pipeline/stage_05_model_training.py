from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.prepare_callbacks import PrepareCallback
from cnnClassifier.components.model_training import ModelTraining
from cnnClassifier import logger


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        logger.info(f"Stage {STAGE_NAME} started.")

        # Step 1: Prepare Callbacks
        logger.info("Preparing callbacks...")
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        logger.info("Callbacks prepared successfully.")

        # Step 2: Set up and train the model
        logger.info("Setting up training configuration...")
        training_config = config.get_training_config()
        training = ModelTraining(config=training_config)

        logger.info("Loading the base model...")
        training.get_base_model()

        logger.info("Generating training and validation data...")
        training.train_valid_generator()

        logger.info("Starting training...")
        training.train(callback_list=callback_list)
        logger.info(f"Training completed successfully for stage {STAGE_NAME}.")


if __name__ == '__main__':
    try:
        # Running the training pipeline
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        # Exception handling with logs
        logger.exception(f"An error occurred during the {STAGE_NAME} pipeline.")
        raise e
