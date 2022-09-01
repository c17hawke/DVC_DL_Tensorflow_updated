from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger

STAGE_NAME = 'Prepare Base Model'

def main():
    config  =  ConfigurationManager()
    base_model_config = config.get_base_model_config()
    base_model = PrepareBaseModel(base_model_config)
    base_model.get_base_model()
    base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info("\n********************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        main()
        logger.info(f"\n>>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e