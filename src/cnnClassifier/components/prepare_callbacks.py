import os
import time
import tensorflow as tf
from cnnClassifier.entity.config_entity import PrepareCallbacksConfig


class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    def _create_tb_callback(self) -> tf.keras.callbacks.TensorBoard:
        """
        Creates a TensorBoard callback with a timestamped log directory.
        """
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        log_dir = os.path.join(self.config.tensorboard_root_log_dir, f"tb_logs_at_{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=log_dir)

    def _create_ckpt_callback(self) -> tf.keras.callbacks.ModelCheckpoint:
        """
        Creates a ModelCheckpoint callback to save the best model.
        """
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True,
            monitor='val_loss',  # You can change this based on your metric
            mode='min',
            verbose=1
        )

    def get_tb_ckpt_callbacks(self) -> list:
        """
        Returns a list of TensorBoard and ModelCheckpoint callbacks.
        """
        return [
            self._create_tb_callback(),
            self._create_ckpt_callback()
        ]
