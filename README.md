# Movie Recommendation
Movie Recommendation API with FastAPI

# Dataset
https://www.kaggle.com/datasets/shubhammehta21/movie-lens-small-latest-dataset

# How does it work
I suggest to use conda to run on your computer. Follow the steps below.

1. Clone this project with :
 ```sh
   git clone https://github.com/Kzis/movie-recommendation.git
   ```
2. Create environment and install environment this project with :
 ```sh
   conda env create -n <YOUR_ENVIRONMENT_NAME> -f environment.yml
   ```
   
   Example 
   
  ```sh
   conda env create -n test_model -f environment.yml
   ```
3. Use cmd to change directory to this project at root path and run command to start project :
 
 ```sh
   uvicorn main:app --reload
   ```
4. Go to http://127.0.0.1:8000/ you will see this message :
 
 ```sh
   {"message":"Hello World"}
   ```
5. If you see this that's so beautiful lol.

#  How to feed input and get output
I suggest to use Swagger-UI to feed input , But you can also use other tools that you are good at, such as Postman or curl.

1. Go to http://localhost:8000/docs you will see this Swagger-UI :
![image](https://user-images.githubusercontent.com/25294734/165154296-68a83605-326b-4b59-bd42-1c3667c0b1e3.png)

2. For /Recommendations endpoint.
   
   Query parameter in url :
   - userd_id (interger)
   - returnMetada (boolean) - Optional parameter

   Curl command example :
   ```sh
      curl -X 'GET' \
     'http://localhost:8000/recommendations/?user_id=11&returnMetadata=true' \
     -H 'accept: application/json'
     ```
   For Swagger-UI you can put Try it out btn and input your parameter and click Excecute btn.
   
   Example output :
   ![image](https://user-images.githubusercontent.com/25294734/165156232-3890d36c-282b-43ec-a1ad-c5910ef53195.png)


3. For /Features endpoint.
   
   Query parameter in url :
   - userd_id (interger)

   Curl command example :
   ```sh
      curl -X 'GET' \
     'http://localhost:8000/features/?user_id=11' \
     -H 'accept: application/json'
     ```
   For Swagger-UI you can put Try it out btn and input your parameter and click Excecute btn.
   
   Example output :
   ![image](https://user-images.githubusercontent.com/25294734/165156375-f2d0734b-5c81-416f-9ebf-5e1c28ab19fc.png)

# How to improve in the future
There are many things to improve for this project.
- Use Redis for load global variable in setting.py file.
- Validation input and handle error.
- Dockerfile for this project.
- Use other model (I have little knowledge in this area).
- Intergrate monitoring system

# Optional

1. This project have a unittest if you want to run use this in root path :

```sh
   pytest
   ```
 should see 6 test is pass.
 
2. This project have loadtest with Locust please start with :
 
 ```sh
    locust -f loadtest.py --host=http://localhost:8000
     
