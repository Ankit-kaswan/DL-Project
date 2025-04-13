import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
        self.model = None
        self.train_generator = None
        self.valid_generator = None

    def get_base_model(self):
        """
        Load the pre-trained (updated) base model.
        """
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)

    def train_valid_generator(self):
        """
        Prepare training and validation data generators with/without augmentation.
        """
        data_generator_kwargs = {
            "rescale": 1.0 / 255,
            "validation_split": 0.20
        }

        dataflow_kwargs = {
            "target_size": self.config.params_image_size[:-1],  # (height, width)
            "batch_size": self.config.params_batch_size,
            "interpolation": "bilinear"
        }

        # Validation generator (no augmentation)
        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(**data_generator_kwargs)

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # Train generator (with augmentation if enabled)
        if self.config.params_is_augmentation:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                **data_generator_kwargs
            )
        else:
            train_data_generator = valid_data_generator

        self.train_generator = train_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """
        Save the trained model to disk.
        """
        model.save(path)

    def train(self, callback_list: list):
        """
        Train the model using the train and validation generators.
        """
        steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=validation_steps,
            callbacks=callback_list
        )

        self.save_model(path=self.config.trained_model_path, model=self.model)
