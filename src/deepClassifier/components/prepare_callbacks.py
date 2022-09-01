from deepClassifier.utils import create_directories
from deepClassifier.entity import PrepareBaseModelConfig
from deepClassifier import logger
import tensorflow as tf
import os
from pathlib import Path
import time


class PrepareCallbacks:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    @staticmethod
    def _get_timestamp():
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    @property
    def _create_tb_callbacks(self):
        timestamp = self._get_timestamp()
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir, f"tb_logs_at_{timestamp}")
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filename=self.config.checkpoint_model_filepath,
            save_best_only=True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
