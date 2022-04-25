import pickle
import setting
from model_development.recsys import create_item_dict , create_user_dict , sample_recommendation_user , create_interaction_matrix

class ModelUtils:
    
    @staticmethod
    def read_model(user_id):
        print("===================")
        print("read_model")
        model_recommend = [74510,76175]
        
        ratings = setting.get_ratings_df()
        movies = setting.get_movies_df()
        
        interactions = create_interaction_matrix(df = ratings,
                                         user_col = 'userId',
                                         item_col = 'movieId',
                                         rating_col = 'rating')
        
        user_dict = create_user_dict(interactions=interactions)
        movies_dict = create_item_dict(df = movies,
                               id_col = 'movieId',
                               name_col = 'title')
        
        loaded_model = pickle.load(open('model_api\movie_rec_model.pickle', 'rb'))
        rec_list = sample_recommendation_user(model = loaded_model, 
                                      interactions = interactions, 
                                      user_id = user_id, 
                                      user_dict = user_dict,
                                      item_dict = movies_dict, 
                                      threshold = 4, 
                                      nrec_items = 10,
                                      show = True)
        print(rec_list)
        return model_recommend 