from utility_package.csv_utlity import *

global dict_links
# global list_ratings
# global list_tags

def init_global_data():
    print("============= init_global_data ======================")
    global dict_movies
    csv_utils = CSVUtils()
    dict_movies = csv_utils.read_movies()
    dict_links = csv_utils.read_links()
    # list_ratings = csv_utils.read_ratings(1)
    # list_tags = csv_utils.read_tags(2)

def get_dict_movies():
    return dict_movies