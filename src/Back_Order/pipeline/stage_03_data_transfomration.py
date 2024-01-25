from Back_Order.config.configuration import ConfigurationManager
from Back_Order.components.data_transformation import DataTransfomration
from Back_Order.logger.logger import logging
import sys
from Back_Order.exception.exception import customexception
from pathlib import Path

STAGE_NAME="DATA TRANSFORMATION STAGE"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        try:
            with open(Path("artifacts/data_validation/result.txt"),'r') as f:
                status=f.read().split(" ")[-1]
            if status == "True":
                config=ConfigurationManager()
                data_transfomration_config=config.get_data_transfomration_config()
                data_transformation=DataTransfomration(config=data_transfomration_config)
                data_transformation.train_test_split()
            else:
                raise Exception("You data schema is not valid")
        except Exception as e:
            print(customexception(e,sys))
                
        
if __name__== "__main__":
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise customexception(e,sys)