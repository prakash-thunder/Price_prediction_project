
# Real Estate Price Prediction Project
## introduction
This project demonstrates a Machine learning model that predicts the home price in Banglore using sklearn and linear regression. It uses the dataset from Kaggle. It also contains a website for interaction with the machine learning model.

### Below data science concepts are used in this project

  - Data loading and cleaning

  - Outlier detection and removal
  
  - Feature engineering
  
  - Dimensionality reduction
  
  - Gridsearchcv for hyperparameter tunning
  
  - K fold cross validation

### Technology and tools used in this project

   - Python
   
   - Numpy and Pandas for data cleaning
   
   - Matplotlib for data visualization
   
   - Sklearn for model building
   
   - Jupyter Notebook
   
   - Python flask for http server
   
   - HTML/CSS/Javascript for UI
## Step
 1.We will first build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com.
 
 2.Second step would be to write a python flask server that uses the saved model to serve http requests.
 
 3.Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price.
    
    Step#1: Import the required libraries
    Step#2: Load the data
    Step#3: Understand the data
           -drop unnecessary columns
    Step#4: Data Cleaning
           - Check for na values
           - Verify unique values of each column
           - Make sure values are correct (eg. 23 BHK home with 2000 Sqrft size is worng)
           - Feature Engineering
           - Dimesionality Reduction
           - Outlier removal using domain knowledge (2bhk price < 3bhk price, size per bhk >= 300 sqft)
           - Outlier removal using standard eviation and mean
           - One Hot encoding
    Step#5: Build Machine Learning Model
    Step#6: Testing The model
    Step#7: Export the model
    Step#8: Export any other important info
## Frontend
- HTML

- CSS

- Javascript

## Backend
- Flask


## Screenshots

![App Screenshot](https://github.com/prakash-thunder/Price_prediction_project/blob/main/model_photo.png?raw=true)


## Dataset Reference
  - Bengaluru House price data
  
  - I have also uploaed the csv file in this repository Bengaluru_House_Data.csv
