import os
from pathlib import Path
from Back_Order.logger.logger import logging
from Back_Order.entity.config_entity import DataIngestionConfig
from Back_Order.utils.common import get_size
import pandas as pd 
import sys
from Back_Order.exception.exception import customexception

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Started")
        try:
            data=pd.read_csv(self.config.source_path)
            logging.info("Reading File")
            os.makedirs(os.path.dirname(os.path.join(self.config.local_file_dir)),exist_ok=True)
            data.to_csv(self.config.local_file_dir,index=False)
        except Exception as e:
            logging.info("Data Ingestion failed")
            raise customexception(e,sys)
        
        