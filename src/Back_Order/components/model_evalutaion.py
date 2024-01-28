import os
import pandas as pd 
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score
from Back_Order.utils.common import save_json
import numpy as np 
import joblib
from Back_Order.entity.config_entity import ModelEValuationConfig
import mlflow
import mlflow.sklearn
from Back_Order.logger.logger import logging
from Back_Order.exception.exception import customexception
from urllib.parse import urlparse
import sys
from pathlib import Path



class ModelEvaluation:
    def __init__(self,config=ModelEValuationConfig):
        self.config=config
    def eval_metrics(self,actual,preds):
        accuracy=accuracy_score(actual,preds)
        f1=f1_score(actual,preds)
        precision=precision_score(actual,preds)
        recall=recall_score(actual,preds)
        return accuracy,f1,precision,recall
    def initiate_model_evaluation(self):
        test_data=pd.read_csv(self.config.test_data_path)
        model=joblib.load(self.config.model_path)
        mlflow.set_registry_uri("")   #Dax hub
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme
        logging.info("Model has registered")
        print(tracking_url_type_store)
        test_x=test_data.drop([self.config.target_column],axis=1)
        maps={"No":0,"Yes":1}
        test_y=test_data[self.config.target_column]
        maps={"No":0,"Yes":1}
        test_y=test_y.map(maps)
        logging.info("Data PRepared for Evaluation")
        
        with mlflow.start_run():
            preds = model.predict(test_x)
            (accuracy,f1,precision,recall) = self.eval_metrics(test_y, preds)
            scores = {"Accuracy":accuracy,"f1_score":f1,"Precision":precision,"Recall":recall}
            save_json(path=Path(self.config.metric_file_name), data=scores)   
            mlflow.log_metric("accuracy",accuracy)
            mlflow.log_metric("f1",f1)
            mlflow.log_metric("precision",precision)
            mlflow.log_metric("recall",recall)
            if tracking_url_type_store !="file":
                mlflow.sklearn.log_model(model,"model",registered_model_name="ml_model")
            else :
                mlflow.sklearn.log_model(model,"model")
             
            
            
        
        
        
    
        
