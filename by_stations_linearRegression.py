from joblib import load
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from tqdm import tqdm

import numpy as np
import preprocessing
import pandas as pd


pd.options.mode.copy_on_write = True


def eval_boardings(predictions: pd.DataFrame, ground_truth: pd.DataFrame):
    combined = pd.merge(predictions, ground_truth, on='trip_id_unique_station')
    mse_board = mean_squared_error(combined["passengers_up_x"], combined["passengers_up_y"])
    return mse_board


def get_df_for_test(df):
    df['time_in_station (sec)'] = 0

    for index, row in tqdm(df.iterrows(), total=df.shape[0]):

        if pd.isna(row["door_closing_time"]):
            df.iloc[index, df.columns.get_loc("door_closing_time")] = row["arrival_time"]
            row["door_closing_time"] = row["arrival_time"]

        if not preprocessing.is_time_after(row["door_closing_time"], row["arrival_time"]):
            df.iloc[index, df.columns.get_loc("door_closing_time")], df.iloc[
                index, df.columns.get_loc("arrival_time")] = row["arrival_time"], row[
                "door_closing_time"]

        # passenger_cont_is_int_pos
        if row["passengers_continue"] <= 0:
            df.iloc[index, df.columns.get_loc("passengers_continue")] = 0

        df.iloc[index, df.columns.get_loc('time_in_station (sec)')] = preprocessing.time_difference(row["arrival_time"],
                                                                                                    row[
                                                                                                        "door_closing_time"])

        return df[['time_in_station (sec)', "passengers_continue", "door_closing_time", 'trip_id_unique_station',
                   "station_id"]]


if __name__ == '__main__':

    baseline_model = load('linear_regression_model.joblib')

    df = pd.read_csv(r'/Users/lilachshay/IML/hackathon_2024_public/train_bus_schedule_filtered.csv',
                     encoding="utf-8")

    X = df[['time_in_station (sec)', 'passengers_continue', 'trip_id_unique_station', "station_id"]]
    y = df[['passengers_up']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    X_train['passengers_up'] = y_train["passengers_up"]
    X_y_train_sorted = X_train.sort_values(by='station_id')

    # y_train['passengers_up'] = X_train['passengers_up']
    # X_train = X_train.drop('passengers_up', axis=1)
    #
    X_y_train_grouped = X_y_train_sorted.groupby('station_id')
    model_per_stations_dict = {}
    i = 0

    # grouped_list = list(X_y_train_sorted)

    # Wrap the list with tqdm for a progress bar
    for key, group in tqdm(X_y_train_grouped):
        X_train_model = group[['time_in_station (sec)', 'passengers_continue']]
        y_train_model = group['passengers_up']

        # Create and fit the model
        model = LinearRegression()
        model.fit(X_train_model, y_train_model)
        model_per_stations_dict[key] = model

    # predictions
    df_test = pd.read_csv(r'/Users/lilachshay/IML/hackathon_2024_public/train_bus_schedule_filtered.csv',
                          encoding="utf-8")
    X_test = get_df_for_test(df_test)
    # X_test['passengers_up'] = y_test["passengers_up"]
    X_y_test_sorted = X_test.sort_values(by='station_id')

    # y_train['passengers_up'] = X_train['passengers_up']
    # X_train = X_train.drop('passengers_up', axis=1)
    #
    X_y_test_grouped = X_y_test_sorted.groupby('station_id')

    # preparing the ground truth pd
    # df_gold_standard = pd.DataFrame({
    #     'trip_id_unique_station': X_y_test_sorted["trip_id_unique_station"],
    #     'passengers_up': X_y_test_sorted["passengers_up"]
    # })

    df_predictions = pd.DataFrame(columns=['trip_id_unique_station', 'passengers_up'])
    for key, group in tqdm(X_y_test_grouped):

        X_test_model = group[['time_in_station (sec)', 'passengers_continue']]
        # y_test_model = group['passengers_up']

        if key not in model_per_stations_dict.keys():
            model = baseline_model
            y_station_predict = model.predict(X_test_model)
            y_station_predict = y_station_predict.flatten().astype(float)
        else:
            # Create and fit the model
            model = model_per_stations_dict[key]
            y_station_predict = model.predict(X_test_model)

        # Replace negative values with zero
        y_station_predict = np.where(y_station_predict < 0, 0, y_station_predict)

        # Round predictions to the nearest integer and ensure they are integers
        y_station_predict = np.round(y_station_predict).astype(int)  # Round and convert to int

        # Create a DataFrame with the predictions
        predictions_df = pd.DataFrame({
            'trip_id_unique_station': group['trip_id_unique_station'],
            'passengers_up': y_station_predict
        })

        # Concatenate the predictions with the main DataFrame
        df_predictions = pd.concat([df_predictions, predictions_df], ignore_index=True)

    df_predictions.to_csv('passengers_up_predictions.csv', index=False)

    # Evaluate the model
    # Prepare the ground truth (actual values)
    df_gold_standard = df_test[['trip_id_unique_station', 'passengers_up']]

    # Merge predictions with ground truth
    df_combined = pd.merge(df_predictions, df_gold_standard, on='trip_id_unique_station')

    # Compute MSE
    mse_boarding = mean_squared_error(df_combined["passengers_up_x"], df_combined["passengers_up_y"])
    print(f"MSE for boardings: {mse_boarding}")


