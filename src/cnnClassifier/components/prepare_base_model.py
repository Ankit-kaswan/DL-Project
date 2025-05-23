
from pathlib import Path
import tensorflow as tf
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig
from cnnClassifier import logger


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config
        self.model = None
        self.full_model = None

    def get_base_model(self):
        logger.info("Loading base model: VGG16")
        self.model = tf.keras.applications.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )

        self.save_model(path=self.config.base_model_path, model=self.model)
        logger.info(f"Base model saved at: {self.config.base_model_path}")

    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        logger.info("Preparing full model")

        if freeze_all:
            for layer in model.layers:
                layer.trainable = False
        elif freeze_till is not None and freeze_till > 0:
            for layer in model.layers[:freeze_till]:
                layer.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation="softmax")(flatten_in)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=prediction)

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )

        logger.info("Model compiled successfully")
        full_model.summary()

        # Optional: Save model summary to a file
        with open("model_summary.txt", "w") as f:
            full_model.summary(print_fn=lambda x: f.write(x + "\n"))

        return full_model

    def update_base_model(self):
        logger.info("Updating base model to include classification layers")
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        logger.info(f"Updated model saved at: {self.config.updated_base_model_path}")

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        path.parent.mkdir(parents=True, exist_ok=True)
        model.save(path)
        logger.info(f"Model saved at: {path}")
