from Back_Order.constants import *
from Back_Order.entity.config_entity import (DataIngestionConfig,
                                             DataValidationConfig,
                                             DataTransfomrationConfig,
                                             ModelTrainingConfig,
                                             ModelEValuationConfig)
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
        
    def get_model_training_config(self)->ModelTrainingConfig:
        config=self.config.model_training
        target=self.schema.TARGET_COLUMNS
        params=self.params.RandomForestClassifier
        create_directories([config.root_dir])
        model_training_config=ModelTrainingConfig(
            root_dir=config.root_dir,
            train_data_path=config.train_data_path,
            test_data_path=config.test_data_path,
            model_name=config.model_name,
            target_column=target.name,
            n_estimators=params.n_estimators,
            min_samples_split=params.min_samples_split,
            min_samples_leaf=params.min_samples_leaf,
            max_depth=params.max_depth,
            max_samples=params.max_samples,
            criterion=params.criterion,
            ccp_alpha=params.ccp_alpha
        )
        return model_training_config
    def get_model_evaluation_config(self)->ModelEValuationConfig:
        config=self.config.model_evaluation
        target=self.schema.TARGET_COLUMNS
        create_directories([config.root_dir])
        model_evaluation_config=ModelEValuationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path=config.model_path,
            metric_file_name=config.metric_file_name,
            target_column=target.name
        )   
        return model_evaluation_config 

