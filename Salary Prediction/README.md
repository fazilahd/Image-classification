# Salary Prediction Project
## Overview
This project predicts employee salaries using machine learning models. The application includes data preprocessing, model training, evaluation, and a web-based interface for salary estimation.

## Features
* Data Analysis: Explores employee data including age, gender, department, job title, and more.
* Models: Implements Linear Regression, Support Vector Regression (SVR), and Random Forest Regression to predict salaries.
* Web App: Provides a Streamlit-based interface for real-time salary predictions based on user input.

## Data
The project uses a [dataset](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/employee_attrition_data.csv) with the following columns:

* Age
* Gender
* Department
* Job_Title
* Years_at_Company
* Satisfaction_Level
* Average_Monthly_Hours
* Promotion_Last_5Years
* Salary
* Attrition

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fazilahd/salary-prediction.git

   cd salary-prediction

3. Install required packages:
   ```bash
   pip install -r requirements.txt

## Usage
**1. Data Analysis**: Run the Jupyter Notebook to explore and preprocess the data.

**2. Model Training**: Train and evaluate the models using the provided Python scripts.

**3. Web App**: Start the Streamlit app to predict salaries:
streamlit run app.py

## Video Demo
Watch the demo video to see the project in action:

[Watch the video demo](https://www.youtube.com/watch?v=J0nLGcmZ7Jc)




## Files
* [**employee_attrition_data.csv**](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/employee_attrition_data.csv): Dataset used for training and testing.
* [**salary_prediction_notebook.ipynb**](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/NOTEBOOK.ipynb): Jupyter Notebook for data analysis and model training.
* [**app.py**](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/app.py): Streamlit application for salary prediction.
* [**model.pkl**](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/model.pkl): Saved Linear Regression model.
* [**scaler.pkl**](https://github.com/fazilahd/Salary-Prediction-Project/blob/main/scaler.pkl): Saved StandardScaler object.

## Results
Linear Regression: Mean Absolute Error (MAE) = 17,767.25, Root Mean Squared Error (RMSE) = 20,895.59

SVR: MAE = 17,794.60, RMSE = 20,817.30

Random Forest: MAE = 18,133.08, RMSE = 21,232.98
