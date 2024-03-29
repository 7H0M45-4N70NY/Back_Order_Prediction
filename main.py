from src.Back_Order.logger.logger import logging
from src.Back_Order.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from src.Back_Order.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.Back_Order.pipeline.stage_03_data_transfomration import DataTransformationTrainingPipeline
from src.Back_Order.pipeline.stage_05_model_training import ModelTrainerTrainingPipeline
from src.Back_Order.pipeline.stage_06_model_evaluation import ModelEvaluationTrainingPipeline
from src.Back_Order.exception.exception import customexception
import sys

STAGE_NAME = "Data Ingestion stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
     
STAGE_NAME = "Data Validation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
STAGE_NAME = "Data Transformation stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataTransformationTrainingPipeline()
   data_validation.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)
     
STAGE_NAME = "Model Training stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelTrainerTrainingPipeline()
   model_training.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)


STAGE_NAME= "Model Evlation Stage"
try:
   logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_training = ModelEvaluationTrainingPipeline()
   model_training.main()
   logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)