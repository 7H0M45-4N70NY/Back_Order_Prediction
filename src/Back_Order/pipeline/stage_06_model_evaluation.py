from Back_Order.config.configuration import ConfigurationManager
from Back_Order.components.model_evalutaion import ModelEvaluation
from Back_Order.logger.logger import logging as  logger

STAGE_NAME = "Model Evlaution stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_evaluation_config()
        model_trainer_config = ModelEvaluation(config=model_trainer_config)
        model_trainer_config.initiate_model_evaluation()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e