from fastapi import APIRouter
from typing import Optional
from utility_package.model_utils import *
import setting

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
def get_recommendations(user_id: Optional[int] = None, returnMetadata: Optional[bool] = None):
    response = {}
    # print("===================")
    # print("get_recommendations")
    # print("user id : ",user_id)
    # print("returnMetadata id : ",returnMetadata)
    try:
        if user_id :
            model_utils = ModelUtils()
            movie_id_suggestion = model_utils.read_model(user_id)
            movie_id_suggestion = [int(movie_id_float) for movie_id_float in movie_id_suggestion]
            if returnMetadata:
                response = get_movie_recommendation_with_metadata(movie_id_suggestion)
            else:
                response = get_movie_recommendation(movie_id_suggestion)  
        else:
            response = {"desciption": "user_id is required"}
            
    except Exception as err:
        print(err)
        
    finally:
        return response

def get_movie_recommendation(movie_id_suggestion):
    items_list = []
    for id in movie_id_suggestion:
        id_recommendations = {"id": id}
        items_list.append(id_recommendations)
    response = {"items": items_list}
    return response
    
def get_movie_recommendation_with_metadata(movie_id_suggestion):
    # print("================")
    # print("get_movie_recommendation_with_metadata")
    # print("movie_id_suggestion :" , movie_id_suggestion)
    
    dict_movies = setting.get_dict_movies()
    items_list = []
    for movie_id in movie_id_suggestion:
        dict_description = dict_movies[str(movie_id)]
        title = dict_description['title']
        genres = dict_description['genres']
        item = {
                "id": movie_id,
                "title":title,
                "genres": genres
            }
        items_list.append(item)
    response = {"items": items_list}
    return response