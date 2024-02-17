# Back Order Prediction System

## Overview

The Back Order Prediction System is a machine learning-powered solution designed to predict potential backorders, enhancing inventory management, product merchandising, and customer satisfaction. This project was developed as part of an internship opportunity, with the support of the Neural Platform.

## Key Features

- **Model Training Module:**
  - Utilizes machine learning models for backorder prediction.
  - Sub-components include Data Preprocessing, Feature Selection, Model Training, and Model Evaluation.

- **Data and Model Versioning Module:**
  - Implements DVC (Data Version Control) for tracking data versions.
  - Utilizes MLflow for logging models, evaluation metrics, and parameters.

- **Event Logging Module:**
  - Logs every event within the system for debugging and monitoring.
  - Sub-components include Custom Exception Handling, Logging Methods, and Non-blocking Logging.

## Technologies Used

- Python
- Flask
- MLflow
- DVC
- HTML

## Project Structure

- `model_training/`: Contains scripts for model training and evaluation.
- `data_versioning/`: Manages data versions using DVC.
- `event_logging/`: Handles event logging and error handling.
- `web_interface/`: Implements the user interface using HTML and Flask.

## How to Run

1. Clone the repository: `git clone https://github.com/your-username/back-order-prediction.git`
2. Navigate to the project directory: `cd back-order-prediction`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the application: `python web_interface/app.py`

## Performance Metrics

- Accuracy: Approximately 91.25%
- F1 Score: 0.10
- Precision: 5.41%
- Recall: 72.47%

## Future Enhancements

- Explore advanced machine learning models.
- Implement real-time data ingestion for up-to-date predictions.
- Enhance the user interface for a better user experience.



## License

This project is licensed under the [MIT License](LICENSE).
