from deepClassifier.constants import *
from deepClassifier.entity import DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig, TrainingConfig
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier import logger
import os

class ConfigurationManager:
    def __init__(
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH, 
        secrets_filepath=SECRETS_FILE_PATH):
        self.config = read_yaml(path_to_yaml=config_filepath)
        self.params = read_yaml(path_to_yaml=params_filepath)
        self.secrets = read_yaml(path_to_yaml=secrets_filepath)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info("getting configuration for data ingestion")

        data_ingestion = self.config.data_ingestion
        create_directories([
            Path(data_ingestion.root_dir)
        ])
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_URL=data_ingestion.source_URL,
            local_data_file=Path(data_ingestion.local_data_file),
            unzip_dir=Path(data_ingestion.unzip_dir)
        )

        return data_ingestion_config

    def get_base_model_config(self) -> PrepareBaseModelConfig:
        logger.info("getting configuration for base model preparation")

        prepare_base_model = self.config.prepare_base_model
        create_directories([
            Path(prepare_base_model.root_dir)
        ])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(prepare_base_model.root_dir),
            base_model_filepath=Path(prepare_base_model.base_model_filepath),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            param_image_size=self.params.IMAGE_SIZE,
            param_classes=self.params.CLASSES,
            param_learning_rate=self.params.LEARNING_RATE,
            param_include_top=self.params.INCLUDE_TOP,
            param_weights=self.params.WEIGHTS
        )
        return prepare_base_model_config

    def get_callbacks_config(self) -> PrepareCallbacksConfig:
        logger.info("getting configuration for callbacks")

        prepare_callbacks = self.config.prepare_callbacks
        create_directories([
            Path(prepare_callbacks.tensorboard_root_log_dir),
            Path(os.path.dirname(prepare_callbacks.checkpoint_model_filepath))
        ])
        callbacks_config = PrepareCallbacksConfig(
            root_dir=Path(prepare_callbacks.root_dir),
            tensorboard_root_log_dir=Path(prepare_callbacks.tensorboard_root_log_dir),
            checkpoint_model_filepath=Path(prepare_callbacks.checkpoint_model_filepath)
        )
        return callbacks_config

    def get_training_config(self) -> TrainingConfig:
        logger.info("getting configuration for model training")

        training = self.config.training
        callbacks = self.config.prepare_callbacks
        updated_base_model = self.config.prepare_base_model.updated_base_model_path
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "PetImages")
        params = self.params

        create_directories([
            Path(training.root_dir)
        ])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            updated_base_model_path=Path(updated_base_model),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentating=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE,
            trained_model_path=Path(training.trained_model_path)
        )
        return training_config