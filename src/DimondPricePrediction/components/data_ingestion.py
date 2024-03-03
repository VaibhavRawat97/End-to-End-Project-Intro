# First we'll try to define the skeleton or basic structure of the project and then write the code.
# First we'll load our data inside this file, we'll do this by creating a 'class' to load the data.
# In the class we'll have constructor as well: def __init__(self) and we'll write pass b/c we just 
# want to leave it empty for now.
# Now we'll write another def function initiate_data_ingestion
# After having coded logger and exception we'll import some necesary inbuilt and custom n=made libraries

import pandas as pd
import numpy as np
from DimondPricePrediction.logger import logging
from DimondPricePrediction.exception import customexception
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from pathlib import Path
import os
import sys


class DataIngestionConfig:
    raw_data_path:str=os.path.join("artifacts","raw.csv")
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("data ingestion started")
        
        try:
            data=pd.read_csv(Path(os.path.join("notebooks/data","gemstone.csv")))
            logging.info("I have read the data as df")
            
            os.makedirs(os.path.join(self,ingestion_config.raw_data_path),exists_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Here I have saved the raw dataset in Artifact folder.")
            
            logging.info("Here I have performed train test split")
            
            train_data,test_data=train_test_split(data,test_size=0.25)
            logging.info("train_test_split completed")
            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)
            
            logging.info("Data Ingestion part completed")
            
        except Exception as e:
            logging.info("Exception during occured at data ingestion stage")
            raise customexception(e,sys)
                            
        