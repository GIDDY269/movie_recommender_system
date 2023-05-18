import pandas as pd
import numpy as np
import sys
import difflib

from src.utils import load_object
from src.exception import CustomException


class recommender:
    def __init__(self):
        pass
    
    def predict(self,movie_name):
        
        df = pd.read_csv('artifact/movie_data.csv')
        list_of_all_titles = df['title'].tolist()
        
        similarity_path = 'artifact/similarity.pkl'
        similarity = load_object(similarity_path)
        
        # choose the closest name to the movie in the dataset
        close_movie = difflib.get_close_matches(movie_name,list_of_all_titles)
        movie_index = df[df['title']==close_movie[0]].index.values[0]
        similarity_score = list(enumerate(similarity[movie_index]))
        # sort based on similarity score
        sorted_score = sorted(similarity_score,key=lambda x:x[1],reverse=True)
        # get movie titles
        i=1
        result = []
        for score in sorted_score :
            index = score[0]
            movie_title = df[df.index==index].title.values[0]
            if (i<11) :
                result.append(movie_title)
                i+=1
        return result




        
