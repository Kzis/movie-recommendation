from fastapi import APIRouter

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
async def get_recommendations():
    return recommendations_db