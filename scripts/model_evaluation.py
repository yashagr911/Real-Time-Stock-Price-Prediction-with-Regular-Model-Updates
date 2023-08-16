import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib
from models.model_code.HistGradientBoostingRegressor  import create_model
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Datetime'])
    return data

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mape = mean_absolute_percentage_error(y_test, y_pred)

    return rmse, mape


def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

if __name__ == "__main__":
    historical_data_path = "data/processed_data/preprocessed_historical_data.csv"

    # Load preprocessed data
    historical_data = load_data(historical_data_path)

    # Define features and target
    features = ['PriceChange', 'SMA_5', 'SMA_20', 'BollingerUpper', 'BollingerLower']
    target = 'Close'

    # Split data into train and test sets
    _, test_data = train_test_split(historical_data, test_size=0.2, random_state=42)

    # Define X_test, y_test
    X_test = test_data[features]
    y_test = test_data[target]

    # Load the trained model
    model = create_model()
    model = joblib.load("models/saved_models/trained_model.pkl")

    # Evaluate the model
    rmse, mape = evaluate_model(model, X_test, y_test)
    
    print("Root Mean Squared Error:", rmse)
    print("Mean Absolute Percentage Error:", mape)
