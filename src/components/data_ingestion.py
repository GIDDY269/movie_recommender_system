import sys
sys.path.append('C:/movierecommender')
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
import numpy as np

from dataclasses import dataclass
from src.components.data_transformation import Datatransformation
from src.components.data_transformation import DataTransformconfig
from src.components.model_trainer import cosine_similarity_config
from src.components.model_trainer import CosineSimilarity

@dataclass
class DataIngestionConfig:
    artifact_path = 'C:/movierecommender/artifact'
    movie_data_path = os.path.join(artifact_path, 'movie_data.csv')
    netflix_data_path = os.path.join(artifact_path, 'netflix_raw_data.csv')
class DataIngestion():
    def __init__(self):
        self.ingestionconfig = DataIngestionConfig()
        
    def initiates_data_ingestion(self):
        logging.info('ENTERED INGESTION COMPONENT')
        try:
            # read the data
            netflix_df = pd.read_csv('C:/movierecommender/notebook/data/netflix_titles.csv')
            
            logging.info('read data as dataframe')
            
            os.makedirs(self.ingestionconfig.artifact_path, exist_ok=True)
            os.makedirs(os.path.dirname(self.ingestionconfig.movie_data_path), exist_ok=True)
            
            netflix_df.to_csv(self.ingestionconfig.netflix_data_path,header=True,index=False)

            
            logging.info('Combined data begins')
            movie_data = pd.concat([netflix_df],ignore_index=True)
            movie_data.to_csv(self.ingestionconfig.movie_data_path,header=True,index=False)
            logging.info('Data ingestion complete')
            
            return(self.ingestionconfig.movie_data_path)
            
        except Exception as e:
            raise CustomException(e,sys)
            
            
            
if __name__=='__main__':
    obj = DataIngestion()
    movie_data = obj.initiates_data_ingestion()
    
    
    data_transformation = Datatransformation()
    train_feature_arr,a = data_transformation.initiate_data_transformation(movie_data)
    
    cosine_similarity = CosineSimilarity()
    cosine_similarity.initiate_cosine_similarity(train_feature_arr)
    
    