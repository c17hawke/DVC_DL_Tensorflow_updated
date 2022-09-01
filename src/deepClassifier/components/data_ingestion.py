from deepClassifier.utils import get_size
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from tqdm import tqdm
import os
from zipfile import ZipFile
import urllib.request as request


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Downloading file...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
                )
            logger.info(f"{filename} downloaded! with following info: \n{headers}")
        logger.info(f"Desired file already exists of size: {get_size(self.config.local_data_file)}")

    def _get_updated_list(self, list_of_file: list) -> list:
        return [
            f for f in list_of_file \
            if f.endswith(".jpg") and \
            ("Cat" in f or "Dog" in f)
            ]
    
    def _proccessing(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        # create_directories([os.path.dirname(target_filepath)])
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)
            logger.info(f"removing file: {target_filepath}") 

    def unzip_and_clean(self):
        logger.info("Unzipping file and checking for 0 size file...")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_file = zf.namelist()
            updated_list_of_files = self._get_updated_list(list_of_file)
            print(len(list_of_file), len(updated_list_of_files))
            
            for f in tqdm(updated_list_of_files):
                self._proccessing(zf, f, self.config.unzip_dir)