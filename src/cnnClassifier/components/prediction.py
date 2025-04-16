import numpy as np
import tensorflow as tf
from cnnClassifier.utils.image_utils import load_image_from_path
from cnnClassifier.entity.config_entity import PredictionConfig
from pathlib import Path


class Prediction:
    def __init__(self, config: PredictionConfig):
        """
        Initializes the Prediction class.

        Args:
            config (PredictionConfig): Configuration settings for prediction.
        """
        self.config = config
        self.model = self.load_model(self.config.path_of_model)

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        """
        Loads the trained Keras model from the given path.

        Args:
            path (Path): Path to the saved model.

        Returns:
            tf.keras.Model: Loaded Keras model.
        """
        return tf.keras.models.load_model(path)

    def predict(self, image_path: str) -> dict:
        """
        Runs the prediction on the image at the given path.

        Args:
            image_path (str): Path to the image for prediction.

        Returns:
            dict: Prediction result containing the predicted label and confidence.
        """
        # Load and preprocess the image
        img_array = load_image_from_path(image_path, target_size=self.config.image_size, color_mode="rgb")

        # Make predictions using the loaded model
        predictions = self.model.predict(img_array)

        # Get the predicted class index and corresponding label
        predicted_index = np.argmax(predictions, axis=1)[0]
        predicted_label = self.config.class_names[predicted_index]

        # Get the confidence level (maximum probability)
        confidence = float(np.max(predictions))

        return {"prediction": predicted_label, "confidence": confidence}
