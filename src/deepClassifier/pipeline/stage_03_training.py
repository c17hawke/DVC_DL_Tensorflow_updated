from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallbacks, Training
from deepClassifier import logger

STAGE_NAME = 'Training'

def main():
    config  =  ConfigurationManager()

    callback_config = config.get_callbacks_config()
    callbacks = PrepareCallbacks(callback_config)
    callback_list = callbacks.get_tb_ckpt_callbacks()

    training_config = config.get_training_config()
    training = Training(training_config)
    training.get_base_model()
    training.train_valid_generator()  
    training.train(
        callback_list=callback_list
    )


if __name__ == "__main__":
    try:
        logger.info("\n********************")
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        main()
        logger.info(f"\n>>>>> stage {STAGE_NAME} completed!<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e