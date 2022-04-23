from fastapi.testclient import TestClient
from main import app

import sys
sys.path.append('../.')

client = TestClient(app)

def test_get_recommendations_without_userid():
    response = client.get("/recommendations")
    assert response.status_code == 200
    assert response.json() == {"desciption": "user_id is required"}
    
def test_get_recommendations_with_userid():
    response = client.get("recommendations/?user_id=18")
    actual = response.json()['items']
    expected = 0
    
    assert len(actual) > expected
    
def test_get_recommendations_with_userid_and_metadata():
    response = client.get("recommendations?user_id=18&returnMetadata=true")
    actual = response.json()
    expected = 0
    
    assert len(actual['items']) > expected
    assert len( actual['items'][0]['title']) > expected
    assert len(actual['items'][0]['genres']) > expected
   

