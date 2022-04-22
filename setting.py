from utility_package.csv_utlity import *

global dict_movies
global dict_links
global list_ratings
global list_tags

def init_global_data():
    csv_utils = CSV_Utility()
    dict_movies = csv_utils.read_movies()
    dict_links = csv_utils.read_links()
    list_ratings = csv_utils.read_ratings(1)
    list_tags = csv_utils.read_tags(2)