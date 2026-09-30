# End-to-End Machine Learning Project

An end-to-end machine-learning application that trains a student performance prediction model and serves predictions through a FastAPI web application.

## Overview

This project demonstrates a complete machine-learning workflow:

- Data ingestion
- Exploratory data analysis
- Data transformation and preprocessing
- Model training and evaluation
- Prediction pipeline creation
- FastAPI-based web deployment

The application accepts student demographic and academic information, including reading and writing scores, and returns a predicted mathematics score.

## Features

- Reusable training and prediction pipelines
- Data preprocessing with scikit-learn
- Support for CatBoost and XGBoost models
- Persisted preprocessing and trained-model artifacts
- FastAPI web interface rendered with Jinja2 templates
- Structured logging and exception handling
- Python package configuration through `setup.py`

## Project Structure

```text
mlproject/
├── app.py                    # FastAPI application and prediction endpoints
├── artifacts/                # Generated data, preprocessing, and model artifacts
├── notebook/                 # Notebooks for exploration and experimentation
├── src/
│   ├── components/           # Data ingestion, transformation, and model training
│   ├── pipeline/             # Training and prediction pipeline orchestration
│   ├── exception.py           # Custom exception handling
│   ├── logger.py              # Application logging configuration
│   └── utils.py               # Shared utility functions
├── templates/                # HTML templates used by the FastAPI application
├── requirements.txt           # Python dependencies
├── setup.py                   # Package installation configuration
└── README.md
```

## Input Features

The prediction form uses the following fields:

- Gender
- Race/ethnicity
- Parental level of education
- Lunch type
- Test preparation course
- Reading score
- Writing score

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/anushka12-u/mlproject.git
cd mlproject
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv venv
venv\\Scripts\\activate
```

**macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

To install the project as a local package, run:

```bash
pip install -e .
```

## Running the Application

Start the FastAPI application with:

```bash
python app.py
```

Alternatively, run it with Uvicorn:

```bash
uvicorn app:app --reload
```

Then open the application in your browser at:

```text
http://localhost:8000
```

The prediction page is available at:

```text
http://localhost:8000/predict
```

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/` | Displays the landing page. |
| `GET` | `/predict` | Displays the prediction form. |
| `POST` | `/predict` | Generates a prediction from submitted student data. |

## Machine-Learning Workflow

1. **Data ingestion** loads the source dataset.
2. **Data transformation** prepares numerical and categorical features for modeling.
3. **Model training** evaluates candidate regression models and saves the best model.
4. **Prediction** loads the saved preprocessing object and model to generate predictions for new input data.
5. **Web serving** exposes the prediction workflow through a FastAPI interface.

## Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- CatBoost
- XGBoost
- Matplotlib and Seaborn
- FastAPI
- Uvicorn
- Jinja2

## Notes

- Model and preprocessing files are generated under the `artifacts/` directory during the training workflow.
- Ensure the required model artifacts exist before submitting a prediction through the web application.
- The first run may take longer while dependencies are installed and models are trained.

## License

This project is available for educational and demonstration purposes.
