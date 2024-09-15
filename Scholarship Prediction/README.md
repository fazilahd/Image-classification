# Scholarship Prediction

## Overview

The **Scholarship Prediction** project aims to predict the likelihood of receiving a scholarship based on various features, including exam scores, country, university, faculty, and department. This project involves data preprocessing, analysis, model building, and deployment using FastAPI.

## Dataset

The dataset used is `erasmus.csv`, with the following columns:

- `Countries`: Country where the university is located.
- `Universities`: Name of the university.
- `Faculties`: Faculty to which the department belongs.
- `Departments`: Department within the faculty.
- `Exam score`: The exam score of the applicant.
- `Grant`: Whether the scholarship was granted (1) or not (0).

### Sample Data

Here is a sample from the dataset:

| Countries | Universities                             | Faculties                      | Departments                             | Exam score | Grant |
|-----------|------------------------------------------|--------------------------------|-----------------------------------------|------------|-------|
| Italia    | UNIVERSITA DEGLI STUDI DI ROMA LA SAPIENZA | FACULTY OF ARTS AND SCIENCES   | ENGLISH LANGUAGE AND LITERATURE          | 98.50      | 1     |
| Italia    | ALMA MATER STUDIORUM - UNIVERSITA DI BOLOGNA | FACULTY OF ARTS AND SCIENCES   | SOCIOLOGY                                | 97.10      | 1     |
| German    | UNIVERSITAET BIELEFELD                   | FACULTY OF ARTS AND SCIENCES   | PSYCHOLOGY                               | 96.80      | 1     |
| German    | HOCHSCHULE FUR ANGEWANDTE WISSENSCHAFTEN HAMBURG | FACULTY OF HEALTH SCIENCES    | NUTRITION AND DIETETICS                  | 96.50      | 1     |
| Italia    | UNIVERSITA DEGLI STUDI DI ROMA LA SAPIENZA | FACULTY OF ARTS AND SCIENCES   | ENGLISH LANGUAGE AND LITERATURE          | 96.32      | 1     |

## Data Processing

- **Missing Values**: Removed rows with missing values.
- **Column Renaming**: Renamed columns for clarity.
- **Encoding**: Encoded categorical variables using `LabelEncoder`.
- **Feature Selection**: Dropped unnecessary columns.

## Data Analysis

- Visualized average exam scores by country.
- Analyzed exam scores by department.

## Model

A **Logistic Regression** classifier was used to predict the likelihood of receiving a scholarship. The model was developed through the following steps:

1. **Data Preparation**: Encoded categorical features and selected relevant features.
2. **Model Training**: Trained the Logistic Regression model.
3. **Evaluation**: Evaluated model performance using accuracy, precision, recall, and F1-score.

## API with FastAPI

A **FastAPI** application serves the predictive model, enabling users to interact with the model through HTTP requests.

### API Endpoints

- **POST /predict**: Predicts the probability of receiving a scholarship based on exam score, country, and department.

### Running the API

1. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload

2. Access the API documentation at:
    ```bash
   http://127.0.0.1:8000/docs

## Video Demo
Watch the video demo:
[Scholarship Prediction Project Demo](https://www.youtube.com/watch?v=IVJ8dfAvKs8)


   
