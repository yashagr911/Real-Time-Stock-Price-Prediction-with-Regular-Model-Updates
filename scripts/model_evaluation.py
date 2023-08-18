import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import joblib
from models.model_code.HistGradientBoostingRegressor  import create_model
import numpy as np

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mape = mean_absolute_percentage_error(y_test, y_pred)

    return rmse, mape


def mean_absolute_percentage_error(y_true, y_pred): 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

if __name__ == "__main__":
    current_data_path = "data/processed_data/preprocessed_current_data.csv"

    # Load preprocessed data
    current_data = load_data(current_data_path)

    # Define features and target
    features = ['PriceChange', 'SMA_5', 'SMA_20', 'BollingerUpper', 'BollingerLower']
    target = 'Close'

    # Split data into train and test sets
    _, test_data = train_test_split(current_data, test_size=0.2, random_state=42)

    # Define X_test, y_test
    X_test = test_data[features]
    y_test = test_data[target]

    # Load the trained model
    model_old = create_model()
    model_new = create_model()
    model_old = joblib.load("models/saved_models/trained_model.pkl")
    model_new = joblib.load("models/saved_models/updated_model.pkl")

    # Evaluate the model
    print("Old model")
    rmse, mape_0 = evaluate_model(model_old, X_test, y_test)
    print("Root Mean Squared Error:", rmse)
    print("Mean Absolute Percentage Error:", mape_0)
    print("new model")
    rmse, mape_1 = evaluate_model(model_new, X_test, y_test)

    if  mape_1 < mape_0:
        joblib.dump(model_new, "models/saved_models/trained_model.pkl")
        print("trained_model updated")
    
    print("Root Mean Squared Error:", rmse)
    print("Mean Absolute Percentage Error:", mape_1)
