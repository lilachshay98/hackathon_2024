  # Hackathon 2024 - Optimizing public Transportation

This project implements a machine learning model to predict the number of passengers boarding a bus at each station. The model is trained using historical bus schedule data and employs linear regression for prediction. 

## Features
- Data preprocessing to handle missing and inconsistent values.
- Linear regression models trained per station.
- Predictions are stored in a CSV file.
- Evaluates performance using Mean Squared Error (MSE).
- Handles outlier detection and time-based data validation.
  
## Libraries
- matplotlib
- pandas
- seaborn
- sklearn
- numpy
- tqdm
- joblib
- datetime

## Project Structure
```
├── Data_Analysis
│   ├── DataAnalysis.py
│   ├── README.md
│   ├── X_passengers_up.csv
│   ├── X_trip_duration.csv
│   ├── bus_column_description.md
│   └── train_bus_schedule.csv
├── README.md
├── SUBMISSION
│   ├── README.txt
│   ├── USERS.txt
│   ├── code
│   │   ├── hackathon_code
│   │   │   └── DataAnalysis.py
│   │   ├── linear_regression_model.joblib
│   │   ├── main_subtask1.py
│   │   └── requirements.txt
│   ├── linear_regression_model.joblib
│   ├── predictions
│   │   ├── passengers_up_predictions.csv
│   │   └── trip_duration_predictions.csv
│   └── project analysis and summary
│       ├── conclusions_and_suggestions.pdf
│       └── project overview.pdf
├── by_stations_linearRegression.py
├── example_files
│   ├── y_importance_example.csv
│   ├── y_match_example.csv
│   ├── y_passengers_up_example.csv
│   └── y_trip_duration_example.csv
├── linear_regression_model.joblib
├── main.py
├── passengers_up_predictions.csv
├── preprocessing.py
├── second_baseline.py
├── second_model_baseline.py
└── train_bus_schedule_filtered.csv
```
