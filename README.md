
## Movies Recommendation System
This project is a movie recommendation system written in Python. It uses the MovieLens Dataset for movies and ratings. The program uses Pandas (Python data analysis library) to work with the datasets.

## Objective
The main goal of this project is to build a recommendation engine that recommends movies to users based on their preferences and ratings. This project is designed to understand the functioning of a recommendation system. I developed an Item Based Collaborative Filter, which computes similarities between movies using various metrics such as cosine, pearson and jaccard.

## Data Pre-processing
After retrieving data from the movies.csv and ratings.csv datasets, I converted the movieId and userId columns into integers.I also created a new column which represents the year of publishing the movie, also I removed the special charecters from movienames using regex. I then converted the matrix into a sparse matrix to be fed into the nearest neighbor model.

## Collaborative Filtering
Collaborative Filtering involves suggesting movies to the users that are based on collecting preferences from many other users. For example, if a user A likes to watch action films and so does user B, then the movies that user B will watch in the future will be recommended to A and vice-versa. Therefore, recommending movies is dependent on creating a relationship of similarity between the users or the movies.

## the Web Application
I built the web application using streamlit library which is a python library to build web applications fast and easy

The web application can be found on https://rte.onrender.com/
