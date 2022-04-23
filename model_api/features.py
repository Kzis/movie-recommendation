from fastapi import APIRouter
from utility_package.csv_utlity import *
from typing import Optional

router = APIRouter(
    prefix="/features",
    tags=["Features"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
def get_features(user_id: Optional[int] = None):
    response = {}
    histories_list=[]
    try:
        if user_id :
            csv_utils = CSVUtils()
            list_ratings = csv_utils.read_ratings(user_id)
            histories = {"histories": list_ratings}
            histories_list.append(histories)
            response = {"features":histories_list}
        else:
            response = {"desciption": "user_id is required"}
    except Exception as err:
        print(err)
    finally:
        return response