from utility_package.csv_utlity import *
from model_development.recsys import *

def init_global_data():
    print("============= init_global_data ======================")
    global dict_movies
    global ratings_df
    global movies_df
    global interactions
    global threshold_rating
      
    csv_utils = CSVUtils()
    dict_movies = csv_utils.read_movies()
    # dict_links = csv_utils.read_links()
    # list_ratings = csv_utils.read_ratings(1)
    # list_tags = csv_utils.read_tags(2)
    ratings_df = csv_utils.read_ratings_df()
    movies_df = csv_utils.read_movies_df()
    
    interactions = create_interaction_matrix(df = ratings_df,
                                         user_col = 'userId',
                                         item_col = 'movieId',
                                         rating_col = 'rating')
    
    threshold_rating = 4
        
    
def get_dict_movies():
    return dict_movies

def get_ratings_df():
    return ratings_df

def get_movies_df():
    return movies_df

def get_interactions_matrix():
    return interactions

def get_threshold_rating():
    return threshold_rating


