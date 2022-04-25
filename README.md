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
I suggest to use Swagger-UI to feed input , But you can also use other tools that you are good at, such as Postman or curl

1. Go to http://localhost:8000/docs you will see this Swagger-UI :
![image](https://user-images.githubusercontent.com/25294734/165154296-68a83605-326b-4b59-bd42-1c3667c0b1e3.png)

# Technology
- Python 3.6
- Flask
- Tensorflow 1.15.0
