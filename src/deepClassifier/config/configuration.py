from deepClassifier.constants import *
from deepClassifier.entity import DataIngestionConfig
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
        self._create_artifact_root()

    def _create_artifact_root(self):
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        logger.info("getting configuration for data ingestion")

        data_ingestion = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_URL=data_ingestion.source_URL,
            local_data_file=Path(data_ingestion.local_data_file),
            unzip_dir=Path(data_ingestion.unzip_dir)
        )

        return data_ingestion_config