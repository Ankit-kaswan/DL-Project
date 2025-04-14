import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import EvaluationConfig
from cnnClassifier.utils.file_utils import save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config
        self.score = None
        self.valid_generator = None

    def _valid_generator(self):
        """
        Prepares the validation data generator.
        """
        data_generator_kwargs = {
            "rescale": 1. / 255,
            "validation_split": 0.30
        }

        dataflow_kwargs = {
            "target_size": self.config.params_image_size[:-1],
            "batch_size": self.config.params_batch_size,
            "interpolation": "bilinear"
        }

        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(**data_generator_kwargs)

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        """
        Load a trained Keras model from the given path.
        """
        return tf.keras.models.load_model(path)

    def evaluation(self):
        """
        Evaluate the trained model and save the results.
        """
        model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = model.evaluate(self.valid_generator)

    def save_score(self):
        """
        Save the evaluation scores to a JSON file.
        """
        scores = {
            "loss": round(self.score[0], 4),
            "accuracy": round(self.score[1], 4)
        }

        # Default to 'scores.json' if config path not provided
        score_path = getattr(self.config, "score_file_path", Path("scores.json"))
        save_json(path=score_path, data=scores)
