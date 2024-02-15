import joblib
import pandas as pd
import numpy as np
from pathlib import Path
from Back_Order.components.data_transformation import DataTransfomration
from Back_Order.config.configuration import ConfigurationManager
from Back_Order.logger.logger import logging
from Back_Order.exception.exception import customexception
import sys
from sklearn.preprocessing import StandardScaler


class PredictionPipeline:
    def __init__(self):
        self.model=joblib.load("artifacts/model_training/model.joblib")
    def predict(self,data):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transfomration_config()
            preprocessor=DataTransfomration(config=data_transformation_config)
            transformed_data=preprocessor.run_transformation_predict(data)
            model_names=list(self.model.feature_names_in_)
            prediction=self.model.predict(transformed_data[model_names])
            result= np.where(prediction==1,"Yes","No")
            return result
        except Exception as e:
            raise customexception(e,sys)
class CustomData:
    def __init__(self,
                 national_inv:float ,
                 lead_time: float ,
                 in_transit_qty:float ,
                 forecast_3_month:float,
                 sales_1_month:float,
                 min_bank:float,
                 pieces_past_due:float,
                 perf_6_month_avg:float,
                 local_bo_qty:float,
                 potential_issue:str,
                 deck_risk:str,
                 oe_constraint:str,
                 ppap_risk:str,
                 stop_auto_buy:str,
                 rev_stop:str):
        self.national_inv=national_inv
        self.lead_time=lead_time
        self.in_transit_qty=in_transit_qty
        self.forecast_3_month=forecast_3_month
        self.sales_1_month=sales_1_month
        self.min_bank=min_bank
        self.pieces_past_due=pieces_past_due
        self.perf_6_month_avg=perf_6_month_avg
        self.local_bo_qty=local_bo_qty
        self.potential_issue=potential_issue
        self.deck_risk=deck_risk
        self.oe_constraint=oe_constraint
        self.ppap_risk=ppap_risk
        self.stop_auto_buy=stop_auto_buy
        self.rev_stop=rev_stop
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'national_inv':[self.national_inv],
                'lead_time':[self.lead_time],
                'in_transit_qty':[self.in_transit_qty],
                'forecast_3_month':[self.forecast_3_month],
                'sales_1_month':[self.sales_1_month],
                'min_bank':[self.min_bank],
                'pieces_past_due':[self.pieces_past_due],
                'perf_6_month_avg':[self.perf_6_month_avg],
                'local_bo_qty':[self.local_bo_qty],
                'potential_issue':[self.potential_issue],
                'deck_risk':[self.deck_risk],
                'oe_constraint':[self.oe_constraint],
                'ppap_risk':[self.ppap_risk],
                'stop_auto_buy':[self.stop_auto_buy],
                'rev_stop':[self.rev_stop]  
                }
            df = pd.DataFrame(custom_data_input_dict)
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise e   
        
        

        
        
        
        
        
        
        
            