import os
import numpy as np
import pandas as pd
from Back_Order.logger.logger import logging
from Back_Order.entity.config_entity import DataTransfomrationConfig
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OrdinalEncoder,StandardScaler
from sklearn.pipeline import Pipeline
from Back_Order.utils.common import save_bin
from Back_Order.constants import *

class DataTransfomration:
    def __init__(self,config:DataTransfomrationConfig,):
        self.config=config
    def run_transformation(self,df):
    #   train['lead_time']=train['lead_time'].fillna(train['lead_time'].median())
        drop_cols=['forecast_6_month','forecast_9_month','perf_12_month_avg','sales_3_month','sales_6_month','sales_9_month','sku']
        df.drop(columns=drop_cols,inplace=True)
        
        cat_cols=['potential_issue', 'deck_risk', 'oe_constraint', 'ppap_risk', 'stop_auto_buy', 'rev_stop']
        num_cols=['national_inv', 'lead_time', 'in_transit_qty', 'forecast_3_month', 'sales_1_month', 'min_bank', 'pieces_past_due', 'perf_6_month_avg', 'local_bo_qty']
        num_pipeline=Pipeline(
            steps=[
                ('imputer',SimpleImputer(strategy="median")),
                ('scaler',StandardScaler())
            ])
        potential_issue=['No', 'Yes']
        deck_risk=['No', 'Yes']
        oe_constraint=['No', 'Yes']
        ppap_risk=['No', 'Yes']
        stop_auto_buy=['Yes', 'No']
        rev_stop= ['No', 'Yes']
        cat_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy="most_frequent")),
                ('labelencoder',OrdinalEncoder(categories=[potential_issue,deck_risk,oe_constraint,ppap_risk,stop_auto_buy,rev_stop]))
            ]
        )
        preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,num_cols),
            ('cat_pipeline',cat_pipeline,cat_cols)
        ])
        new_df=preprocessor.fit_transform(df)
        return pd.DataFrame(new_df,columns=df.columns)
    
    def train_test_split(self):
        data=pd.read_csv(self.config.data_path)
        data.dropna(subset=['went_on_backorder'],inplace=True)
        logging.info("Read data File")
        target_column="went_on_backorder"
        y=data[[target_column]]
        x=data.drop(columns=target_column)
        logging.info("Seperated target columns")
        logging.info("Running transfomration on X features")
        transformed_x=self.run_transformation(x)
        logging.info("data Transfomration completed")
        data=pd.concat([transformed_x,y],axis=1)
        train,test=train_test_split(data,test_size=0.2,random_state=1)
        
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)
        logging.info("Splited data into training and test sets")
        logging.info(train.shape)
        logging.info(test.shape)

        over = SMOTE(sampling_strategy=0.1,random_state=1)
        logging.info("Called the smote method")
        under = RandomUnderSampler(sampling_strategy=0.5,random_state=1)
        logging.info("CAlled undersampling")
        X=train.drop(columns=target_column)
        y=train[target_column]
        maps={"No":0,"Yes":1}
        y=y.map(maps)
        x_smoted,y_smoted=over.fit_resample(X,y)
        logging.info("overs ampled data")
        x_combined,y_combined=under.fit_resample(x_smoted,y_smoted)
        logging.info("under sampled data")
        train_new=pd.concat([x_combined,y_combined],axis=1)
        logging.info("Samples are balaced using over and under sampling ")
        train_new.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        logging.info(train_new.shape)
        print(train_new.shape)
        print(test.shape)
        
    def prediction_transformation(self,df2):
    #   train['lead_time']=train['lead_time'].fillna(train['lead_time'].median())
        df=df2
        drop_cols=['forecast_6_month','forecast_9_month','perf_12_month_avg','sales_3_month','sales_6_month','sales_9_month','sku']
        df.drop(columns=drop_cols,inplace=True)
        cat_cols=['potential_issue', 'deck_risk', 'oe_constraint', 'ppap_risk', 'stop_auto_buy', 'rev_stop']
        num_cols=['national_inv', 'lead_time', 'in_transit_qty', 'forecast_3_month', 'sales_1_month', 'min_bank', 'pieces_past_due', 'perf_6_month_avg', 'local_bo_qty']
        num_pipeline=Pipeline(
            steps=[
                ('imputer',SimpleImputer(strategy="median")),
                ('scaler',StandardScaler())
            ])
        potential_issue=['No', 'Yes']
        deck_risk=['No', 'Yes']
        oe_constraint=['No', 'Yes']
        ppap_risk=['No', 'Yes']
        stop_auto_buy=['Yes', 'No']
        rev_stop= ['No', 'Yes']
        cat_pipeline = Pipeline(
            steps=[
                ('imputer', SimpleImputer(strategy="most_frequent")),
                ('labelencoder',OrdinalEncoder(categories=[potential_issue,deck_risk,oe_constraint,ppap_risk,stop_auto_buy,rev_stop]))
            ]
        )
        preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,num_cols),
            ('cat_pipeline',cat_pipeline,cat_cols)
        ])
        new_df=preprocessor.fit_transform(df)
        return pd.DataFrame(new_df,columns=df.columns)
    
        
        
                
        


        
