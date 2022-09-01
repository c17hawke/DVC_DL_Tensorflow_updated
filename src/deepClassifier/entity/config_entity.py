from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "raw_data_URL",
    "raw_zip_filepath",
    "raw_unzipped_dirpath"
])
