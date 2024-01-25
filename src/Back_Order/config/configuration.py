from Back_Order.constants import *
from Back_Order.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransfomrationConfig
from Back_Order.utils.common import read_yaml,create_directories

class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH,
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config=read_yaml(config_filepath)
        self.params=read_yaml(params_filepath)
        self.schema=read_yaml(schema_filepath)
        
        create_directories([self.config.artifacts_root])
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config=self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config=DataIngestionConfig(
            root_dir=config.root_dir,
            source_path=config.source_path,
            local_file_dir=config.local_file_dir
        )
        return data_ingestion_config
    def get_data_validation_config(self)->DataValidationConfig:
        config=self.config.data_validation
        schema=self.schema.COLUMNS
        create_directories([config.root_dir])

        data_validation_config=DataValidationConfig(
            root_dir=config.root_dir,
            target=config.target,
            all_schema=schema,
            result=config.result
        )
        return data_validation_config
    def get_data_transfomration_config(self)->DataTransfomrationConfig:
        config=self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config=DataTransfomrationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path
        )
        return data_transformation_config
        
    

