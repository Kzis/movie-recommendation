from fastapi import APIRouter
from utility_package.csv_utlity import *
from typing import Optional
import setting

router = APIRouter(
    prefix="/features",
    tags=["Features"],
    responses={404: {"message": "Not found"}}
)

# @router.get("/")
# def get_features(user_id: Optional[int] = None):
#     response = {}
#     histories_list=[]
#     try:
#         if user_id :
#             csv_utils = CSVUtils()
#             list_ratings = csv_utils.read_ratings(user_id)
#             histories = {"histories": list_ratings}
#             histories_list.append(histories)
#             response = {"features":histories_list}
#         else:
#             response = {"desciption": "user_id is required"}
#     except Exception as err:
#         print(err)
#     finally:
#         return response
    

@router.get("/")
def get_features(user_id: Optional[int] = None):
    response = {}
    histories_list=[]
    try:
        if user_id :
            interactions = setting.get_interactions_matrix()
            features_list = list(pd.Series(interactions.loc[user_id,:] \
                            [interactions.loc[user_id,:] > setting.get_threshold_rating()].index) \
                            .sort_values(ascending=False))
            features_list = [int(feature_item) for feature_item in features_list]
            histories = {"histories":features_list}
            histories_list.append(histories)
            response = {"features":histories_list}
            # print(len(features_list))
            # print(features_list)
        else:
            response = {"desciption": "user_id is required"}
    except Exception as err:
        print(err)
    finally:
        return response