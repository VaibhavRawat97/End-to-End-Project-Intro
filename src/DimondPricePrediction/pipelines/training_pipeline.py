from DimondPricePrediction.components.data_ingestion import DataIngestion
import os
import sys
from DimondPricePrediction.logger import logging
from DimondPricePrediction.exception import customexception
import pandas as pd 

obj=DataIngestion()

obj.initiate_data_ingestion()