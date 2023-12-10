# Sepsis Prediction FastAPI API

## Overview

This repository contains a FastAPI API for predicting sepsis based on a machine learning model. The model is built using scikit-learn and is available as a joblib pipeline. The API accepts input data related to various health parameters and returns a prediction regarding the likelihood of sepsis.

![Api works](https://github.com/doeabla/Last_project/assets/137217264/d727b03b-cf48-426e-88c4-bf92b61e529d)


## FAST API and Docker
### What is FastAPI?
FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be easy to use and to provide automatic interactive documentation (using Swagger UI and ReDoc) while also being fast to execute. FastAPI is built on top of Starlette and Pydantic, leveraging their capabilities for asynchronous programming and data validation, respectively.


### What is Docker?
Docker is a platform designed to make it easier to create, deploy, and run applications using containers. Containers allow developers to package an application and its dependencies into a single, lightweight unit that can run consistently across various environments. Docker provides a set of tools and a platform for managing these containers.

![api to docker](https://github.com/doeabla/Last_project/assets/137217264/dd057425-f8e3-4c68-83fb-69a67acc1eef)


For this project, datasets provided on [Kaggle](https://www.kaggle.com/datasets/chaunguynnghunh/sepsis) was used. Below are steps followed to create an API and dockerize it.

#### 1. Load and Analyze Data:

* Load the train and test datasets.

* Analyze and preprocess the data.

* Explore the distribution of features and the target variable.

#### 2. Train a Machine Learning Model:

* Split the dataset into features (X) and target (y).

* Balance the dataset 

* Create pipeline 

* Train a machine learning models on the training data.For this project K-Near Neighbours, Decision tree,and Logistic Regression were used. 

#### 3. Save the Model:

* After training the model, save it using joblib so that it can be loaded later for predictions.
![image](https://github.com/doeabla/Last_project/assets/137217264/b98c6e80-aa2d-4dc5-aedc-b2043a513a80)


#### 4. Create FastAPI Application:

* Define the FastAPI application.

* Define a Pydantic model for the input data (InputData).

* Create an endpoint for prediction (predict).

![image](https://github.com/doeabla/Last_project/assets/137217264/e20f9386-d102-4ed6-86f7-704ca544f8d7)

#### 5. Make Predictions with the Model:

In the predict endpoint, input datails received, preprocessed, and the pre-trained model used for predictions.
![image](https://github.com/doeabla/Last_project/assets/137217264/956171d6-a80a-4d7e-822e-ccbc76070d31)

#### 6. Dockerize the Application:

* Write a Dockerfile to containerize your FastAPI application.

* Build the Docker image.

* Run the Docker container.
![image](https://github.com/doeabla/Last_project/assets/137217264/c7f1befe-f510-46ce-ad53-87c5c374ffd0)
![image](https://github.com/doeabla/Last_project/assets/137217264/e8013dd6-4971-4d5f-aa33-7bf322991d3d)


## Setup


1. Clone the repository:

    ```bash
    git clone https://github.com/doeabla/Last_project.git
    cd your-repository
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the FastAPI Server:
    ```bash
    uvicorn main:app --reload
    ```


The API will be accessible at http://0.0.0.0:8000.

## Endpoints
### Home Endpoint
http://0.0.0.0:8000/docs
Provides a welcome message for the Sepsis Prediction App API.

### Prediction Endpoint
http://0.0.0.0:8000/predict
Accepts POST requests with input data for sepsis prediction. Returns the prediction result.

### API after Dockerization
http://localhost:8000/docs

## Input Data Format
The input data for the prediction endpoint should be sent as a POST request in the JSON format with the following structure:
```bash
  {
  "Plasma_glucose": int,
  "Blood_work1": int,
  "Blood_Pressure": int,
  "Blood_work2": int,
  "Blood_work3": int,
  "BMI": float,
  "Blood_work4": float,
  "Age": int,
  "Insurance": int
}
```

## Response Format
The prediction endpoint will return a JSON response with the predicted result:
```bash
    {
  "prediction": "Positive"
}
```

## Note:

1. Make sure to have Python installed.
Ensure that FastAPI and other dependencies are installed using the provided requirements.txt file.
The API runs on http://0.0.0.0:8000 by default.

2. When you run an application from a Docker container, the application becomes accessible on the specified port of the host machine due to the port mapping. This allows you to interact with the application as if it were running directly on the host.
![image](https://github.com/doeabla/Last_project/assets/137217264/a4a268c6-42b8-4957-9899-a004ff8c0cc6)


## Acknowledgements
We would like to thank Azubi Africa for the opportunity to learn how to build an API with FastAPI and furthur dockerize it. The experience has been great. 


## Authors
| Name | GitHub link |
| ---- | ---- |
| Doe Edinam                   | https://github.com/doeabla         |
| Kofi Asare Bamfo             | https://github.com/akbamfo         |
| Enoch Taylor-Nketiah         | https://github.com/kojoboyoo       |
| Philip Tolutope Oludipe       |        |


| Project |	Name |	Published Article |	Deployed|
| ---- | -----| ----- | ----- |
| LP6	| Sepsis API |	[Sepsis API LP6](https://medium.com/@eadoe97/empowering-retail-businesses-the-retail-store-sales-prediction-app-2b0a8fbaba80) | [Sepsis_API](http://localhost:8000/docs#/default/predict_predict_post)
