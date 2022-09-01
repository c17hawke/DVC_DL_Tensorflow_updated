from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", [
    "root_dir",
    "source_URL",
    "local_data_file",
    "unzip_dir"
])

PrepareBaseModelConfig = namedtuple("PrepareBaseModelConfig",[
    "root_dir",
    "base_model_filepath",
    "updated_base_model_path",
    "param_image_size",
    "param_classes",
    "param_learning_rate",
    "param_include_top",
    "param_weights"
])