import sys
sys.path.append('C:/movierecommender')
import os
import pandas as pd
import numpy as np
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from src.utils import save_object




@dataclass 
class DataTransformconfig:
    preprocessor_file_path = os.path.join('artifact','preprocessor.pkl')
    
class Datatransformation:
    def __init__(self):
        self.data_transformation_object = DataTransformconfig()
        self.imp = SimpleImputer(strategy='constant',fill_value=' ')
        self.tfidf = TfidfVectorizer()
    
    def create_data_transformer_object(self,data):
        
        'This functions performs data transformation '
        
        try:
            data = self.imp.fit_transform(data)
            
            # Concatenate all columns into a single text column
            
            data = pd.DataFrame(data).apply(lambda x: ' '.join(x), axis=1)
            # Convert text into a TF-IDF matrix
            
            data = self.tfidf.fit_transform(data)
            
            return data
        except Exception as e :
            raise CustomException(e,sys)
        
    
    def initiate_data_transformation(self,movie_data):
        try :
            df = pd.read_csv(movie_data)
            logging.info('read data')
            logging.info('obtaining preprocessor object')
            
            df['release_year'] = str(df['release_year'])
            selected_features_df = df[['type','title','director','cast','country','release_year','rating','listed_in','description']]
            logging.info(f'columns used : {selected_features_df.columns}')
            
            logging.info('Applying preprocessing object to data')
        
            train_feature_arr = self.create_data_transformer_object(selected_features_df)
            
        
            logging.info('Data transformation complete')
        
            return(train_feature_arr,self.data_transformation_object )
            
        
        except Exception as e:
            raise CustomException(e, sys)        

