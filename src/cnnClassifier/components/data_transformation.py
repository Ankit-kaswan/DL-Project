import os
from cnnClassifier.entity.config_entity import DataTransformationConfig
from cnnClassifier import logger
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def get_data_generators(self):
        logger.info("Starting Data Transformation...")

        train_datagen = ImageDataGenerator(rescale=1./255)
        test_datagen = ImageDataGenerator(rescale=1./255)

        train_generator = train_datagen.flow_from_directory(
            directory=self.config.train_dir,
            target_size=self.config.image_size,
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        test_generator = test_datagen.flow_from_directory(
            directory=self.config.test_dir,
            target_size=self.config.image_size,
            batch_size=self.config.batch_size,
            class_mode='categorical'
        )

        logger.info("Data generators created.")
        return train_generator, test_generator

