# Bike Purchasement Prediction Project

## Overview

This project involves predicting bike purchases based on various customer attributes using machine learning models. The dataset used contains information about customers such as income, age, education, and more. The project includes data preprocessing, model training, and a web application for predictions.

## Files

- [**`Bike Purchasement Streamlit.ipynb`**](https://github.com/fazilahd/Prediction-Models/blob/main/Bike%20Purchasement%20Streamlit/Notebook.ipynb): This Jupyter notebook contains the data exploration, preprocessing, model training, and evaluation. It includes the following steps:
  - Loading and exploring the data.
  - Data cleaning and preprocessing.
  - Model training using Decision Trees and Random Forests.
  - Evaluation of models' performance.
  - Saving the best model for use in the Streamlit app.

- [**`app.py`**](https://github.com/fazilahd/Prediction-Models/blob/main/Bike%20Purchasement%20Streamlit/app.py): This is the Streamlit application file that allows users to input their data and get predictions on whether they are likely to purchase a bike.

- [**`model.pkl`**](https://github.com/fazilahd/Prediction-Models/blob/main/Bike%20Purchasement%20Streamlit/model.pkl): The saved model file which is used by the Streamlit app to make predictions.

## Project Steps

1. **Data Exploration and Preprocessing**:
   - Load and inspect the dataset.
   - Handle missing values and duplicate records.
   - Convert categorical features into numerical values.
   - Split the data into training and testing sets.

2. **Model Training**:
   - Train Decision Tree and Random Forest models.
   - Perform hyperparameter tuning using GridSearchCV.
   - Evaluate model accuracy.

3. **Streamlit Application**:
   - Create a web app using Streamlit to allow users to input their data and get predictions.

## How to Run the Streamlit App

1. Ensure you have the necessary Python packages installed:
   ```bash
   pip install streamlit numpy joblib

2. Run the Streamlit app with the following command:
   ```bash
   streamlit run app.py

3. Open the provided URL in your web browser to interact with the app.

## Demo
For a visual demonstration of the project, click [here](https://youtu.be/26ZGMhJGX5E).
