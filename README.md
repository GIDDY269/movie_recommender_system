

## Movie Recommendation System using Cosine Similarity

This is a content-based movie recommendation system that utilizes cosine similarity to provide personalized movie recommendations based on user preferences. The system analyzes the content of movies, such as genre, plot, and actors,country,release_year and matches them with the user's input to generate recommendations.

********
## HOW IT WORKS

The movie recommendation system uses cosine similarity to measure the similarity between movies. It creates a vector representation for each movie, where each feature represents a specific attribute, such as genre, plot, or actors. The cosine similarity is then calculated between the user's input vector and the vectors of all movies in the database. The system recommends the movies with the highest cosine similarity scores.
****

## INSTALLATION

* Clone the repository

`git clone https://github.com/GIDDY269/movie_recommender_system.git`

****

* Navigate to the project directory

`cd movie_recommender_system`

****

* install the required dependecies

`pip install -r requirements.txt`

****

* Run the streamlit app

`streamlit run 'app.py'`

## USAGE

* Just type in the movie you want recommendation for and click `recommend`

![image](https://raw.githubusercontent.com/GIDDY269/movie_recommender_system/main/image/Screenshot68.png)


* link to try it out : https://giddy269-movie-recommender-system-app-u7ibrr.streamlit.app/ 