from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/recommendations",
    tags=["Recommendations"],
    responses={404: {"message": "Not found"}}
)

recommendations_db = [
    {
        "title": "The C Programming",
        "test": 1236
    },
    {
        "title": "Learn Python the Hard Way",
        "test": 4566
    }
]


@router.get("/")
async def xxx():
    return recommendations_db

@router.get("/{user_id}/")
def get_recommendations(user_id: int, returnMetadata: Optional[bool] = None):
    recommendations = {"user_id": user_id}

    if returnMetadata:
        recommendations.update({"meta_data": returnMetadata})
        recommendations.update({"meta_data_desc": "This is the meta_data"})

    return recommendations