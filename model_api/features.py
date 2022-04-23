from fastapi import APIRouter
from utility_package.model_utils import *

router = APIRouter(
    prefix="/features",
    tags=["Features"],
    responses={404: {"message": "Not found"}}
)

@router.get("/")
def get_features():
    return {"test" : "xxxx"}