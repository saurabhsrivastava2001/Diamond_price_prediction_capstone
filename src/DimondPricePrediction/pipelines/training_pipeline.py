import os
import sys

sys.path.append("D:\\Desktop\\DiamondPricePrediction-main\\src")

from DimondPricePrediction.components.data_ingestion import DataIngestion
from DimondPricePrediction.components.data_transformation import DataTransformation
from DimondPricePrediction.components.model_trainer import ModelTrainer

sys.path.append("D:\\Desktop\\DiamondPricePrediction-main\\src\\DimondPricePrediction")
from DimondPricePrediction.logger import logging as logger

from exception import Customexception
import pandas as pd


obj=DataIngestion()

train_data_path,test_data_path=obj.initiate_data_ingestion()

data_transformation=DataTransformation()

train_arr,test_arr=data_transformation.initialize_data_transformation(train_data_path,test_data_path)


model_trainer_obj=ModelTrainer()
model_trainer_obj.initate_model_training(train_arr,test_arr)

