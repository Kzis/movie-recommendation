from fastapi.testclient import TestClient

# from model_api.main import app

import sys
sys.path.append('./../model_api')
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    

if __name__ == '__main__':
   test_read_main()  