from fastapi.testclient import TestClient
from main import app
from utility_package.csv_utlity import *

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
    actual = csv_utils.read_ratings(18)
    expected = response.json()['features'][0]['histories']
    
    assert 502 == len(expected)
    assert actual == expected
