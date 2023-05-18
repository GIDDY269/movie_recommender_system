import pandas as pd
import numpy as np
import sys
sys.path.append('C:/movierecommender')
import os
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from sklearn.metrics.pairwise import cosine_similarity

@dataclass
class cosine_similarity_config :
    similarity_object_data_path = os.path.join('artifact','similarity.pkl')
    
class CosineSimilarity:
    def __init__(self):
        self.cosine_similarity_object = cosine_similarity_config()
    def initiate_cosine_similarity(self, train_feature_arr):
        try :
            logging.info('initiatizing cosine similarity')
            cos_sim = cosine_similarity(train_feature_arr)
            save_object(file_path=self.cosine_similarity_object.similarity_object_data_path,obj=cos_sim)
            logging.info('cosine similarity done')
            
            save_object(file_path=self.cosine_similarity_object.similarity_object_data_path, obj=cos_sim)
            
            logging.info('similarity saved')
            return (cos_sim,self.cosine_similarity_object)
        except Exception as e :
            raise CustomException(e,sys)