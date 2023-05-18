import streamlit as st
import numpy as np
from src.pipeline.predict_pipeline import recommender
import pandas as pd
import wikipediaapi
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# YouTube API key
API_KEY = 'AIzaSyBRNPGcuiEYLxTX3ijHetXiObPWJxeQr5g'

# Wikipedia API
wiki = wikipediaapi.Wikipedia('en')

# Movie data
movie = pd.read_csv('artifact/movie_data.csv')

def get_video_id(movie_title):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    search_response = youtube.search().list(
        q=movie_title + ' trailer',
        part='id,snippet',
        maxResults=1,
        type='video'
    ).execute()
    video_id = search_response['items'][0]['id']['videoId']
    return video_id

st.title('MOVIE RECOMMENDER SYSTEM')

option = st.selectbox(
    "ENTER MOVIE MOVIE",
    (movie['title'])
)

if st.button('recommend movies'):
    if option:
        recommend = recommender()
        result = recommend.predict(option)
        st.header(' YOU WOULD LOVE TO WATCH THESE ')
        
        # Display the recommended movies and trailers
        for title in result:
            # Search wikipedia for the movie title
            page = wiki.page(title)
            if page.exists():
                # If the wikipedia page exists, create a hyperlink to it
                st.write(f"[{title}]({page.fullurl})")
            else:
                # If the wikipedia page doesn't exist, display the title without a hyperlink
                st.write(title)
                
            # Display the movie trailer using YouTube API
            video_id = get_video_id(title)
            st.write(f'<iframe width="500" height="315" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
