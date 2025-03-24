  # Hackathon 2024 - Optimizing public Transportation

This project implements a machine learning model to predict the number of passengers boarding a bus at each station. The model is trained using historical bus schedule data and employs linear regression for prediction. 

## Features
- Data preprocessing to handle missing and inconsistent values.
- Linear regression models trained per station.
- Predictions are stored in a CSV file.
- Evaluates performance using Mean Squared Error (MSE).
- Handles outlier detection and time-based data validation.
- Implements grouping of predictions by `trip_id_unique_station`.
  
## Getting Started
Ensure you have the following dependencies installed:

```bash
pip install numpy pandas scikit-learn tqdm joblib


