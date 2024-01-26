from Back_Order.logger.logger import logging
from Back_Order.entity.config_entity import ModelTrainingConfig
import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

class ModelTrainer:
    def __init__(self,config:ModelTrainingConfig):
        self.config=config
    def train(self):
        train_data=pd.read_csv(self.config.train_data_path)
        test_data=pd.read_csv(self.config.test_data_path)     
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        model=RandomForestClassifier(n_estimators=self.config.n_estimators,
                                     min_samples_leaf=self.config.min_samples_leaf,
                                     min_samples_split=self.config.min_samples_split,
                                     max_samples=self.config.max_samples,
                                     max_depth=self.config.max_depth,
                                     criterion=self.config.criterion,
                                     ccp_alpha=self.config.ccp_alpha
                                     )
        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        