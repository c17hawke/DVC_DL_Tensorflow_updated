from deepClassifier.utils import create_directories
from deepClassifier.entity import PrepareBaseModelConfig
from deepClassifier import logger
import tensorflow as tf
import io
from pathlib import Path



class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
        logger.info(f"model saved at: {path}")

    def get_base_model(self, model_name: str="VGG16"):
        logger.info(f"creating base model for transfer learning...")
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.param_image_size,
            weights=self.config.param_weights,
            include_top=self.config.param_include_top
        )
        model_path = self.config.base_model_filepath

        self.save_model(path=model_path, model=self.model)
        logger.info(f"base model: {model_name} saved!")

    
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            logger.info("freeze all the layers of base CNN layer")
            for layer in model.layers:
                layer.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            logger.info(f"freeze the layers of base CNN layer till {freeze_till}")
            for layer in model.layers[:-freeze_till]:
                layer.trainable = False

        ## add our fully connected layers
        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(
            optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss = tf.keras.losses.CategoricalCrossentropy(),
            metrics = ["accuracy"]
        )

        logger.info("custom model is compiled and ready to be trained")
        full_model.summary()
        return full_model

    @staticmethod
    def _log_model_summary(full_model):
        with io.StringIO() as stream:
            full_model.summary(print_fn=lambda x: stream.write(f"{x}\n"))
            summary_str = stream.getvalue()
        return summary_str

    def update_base_model(self):
        logger.info(f"creating custom model for transfer learning")
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.param_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.param_learning_rate
        )


        logger.info(f"full model summary: \n{self._log_model_summary(self.full_model)}")

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)
        logger.info(f"custom model saved!")

