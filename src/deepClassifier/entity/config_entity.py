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

PrepareCallbacksConfig = namedtuple("PrepareCallbacksConfig",[
    "root_dir",
    "tensorboard_root_log_dir",
    "checkpoint_model_filepath"
])


TrainingConfig = namedtuple("TrainingConfig",[
    "root_dir",
    "updated_base_model_path",
    "training_data",
    "params_epochs",
    "params_batch_size",
    "params_is_augmentating",
    "params_image_size",
    "trained_model_path"
])