from fastapi.testclient import TestClient
from main import app
from utility_package.csv_utlity import *
import setting

import sys
sys.path.append('../.')

client = TestClient(app)

def test_get_features_without_userid():
    response = client.get("/features")
    assert response.status_code == 200
    assert response.json() == {"desciption": "user_id is required"}
    
def test_get_features_with_userid():
    response = client.get("/features/?user_id=18")
    csv_utils = CSVUtils()
    ratings = csv_utils.read_ratings_df()
    unsort_actual =  ratings.loc[((ratings.rating>setting.get_threshold_rating()) & (ratings.userId==18))].movieId.to_list()
    actual = sorted([int(ele) for ele in unsort_actual], reverse=True)
    expected = response.json()['features'][0]['histories']
    
    assert len(actual) == len(expected)
    assert actual == expected
