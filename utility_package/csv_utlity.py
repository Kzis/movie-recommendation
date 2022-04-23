
import csv
import pandas as pd
from pathlib import Path
from os import path
UP_PATH = Path(__file__).parents[1]
file_path = path.join(UP_PATH, "data\\movielens_small_main\\")

class CSVUtils:
    
    @staticmethod
    def read_movies():
        dict_movie = {}
        with open(file_path + 'movies.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dict_movie[row["movieId"]] = {
                    "title" : row["title"],
                    "genres" :  row["genres"]
                }
            return dict_movie     
        
    @staticmethod
    def read_links():
        dict_links = {}
        with open(file_path + 'links.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dict_links[row["movieId"]] = {
                    "imdbId" : row["imdbId"],
                    "tmdbId" :  row["tmdbId"]
                }
            return dict_links 
        
    @staticmethod
    def read_ratings(userId):
        with open(file_path + 'ratings.csv', newline='') as csvfile:
            df = pd.read_csv(csvfile)
            df_ratings = df[ df["userId"] == userId]
            return [int(ele) for ele in df_ratings.movieId.to_list()]    
        
    @staticmethod
    def read_tags(userId):
        with open(file_path + 'tags.csv', newline='') as csvfile:
            df = pd.read_csv(csvfile)
            df_tags = df[ df["userId"] == userId]
            return [int(ele) for ele in df_tags.movieId.to_list()]   
