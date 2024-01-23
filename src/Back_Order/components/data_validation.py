import os
import pandas as pd
from Back_Order.logger.logger import logging as  logger
from Back_Order.entity.config_entity import DataValidationConfig
import sys
from Back_Order.exception.exception import customexception


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config
        
    def validate_all_columns(self)->bool:
        try:
            validation_status=None
            train=pd.read_csv(self.config.target)
            all_schema=self.config.all_schema
            
            for i,j in all_schema.items():
                if i in train.columns and train[i].dtype==j:
                    validation_status=True
                    with open(self.config.result,'w') as f:
                        f.write(f"Validation Status : {validation_status}")
                else:
                    validation_status=False
                    with open(self.config.result,'w') as f:
                        f.write(f"Validation Status : {validation_status}")
                        
            return validation_status
        except Exception as e:
            raise customexception(e,sys)
            
            
            