from src.Back_Order.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransfomrationConfig
from src.Back_Order.config.configuration import ConfigurationManager

class DataTransfomration:
    def __init__(self,config:DataTransfomrationConfig,):
        self.config=config
    def prints(self):
        print(self.config.target_path)
from src.Back_Order.config.configuration import ConfigurationManager
the_config=ConfigurationManager()
ts_config=the_config.get_data_transfomration_config()
obj=DataTransfomration(config=ts_config)
obj.prints()