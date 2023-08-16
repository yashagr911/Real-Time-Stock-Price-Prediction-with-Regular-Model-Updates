import pandas as pd
from models.model_code.HistGradientBoostingRegressor  import create_model
import joblib

def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Datetime'])
    return data

def update_model(model, X_new, y_new):
    model.fit(X_new, y_new)
    return model

if __name__ == "__main__":
    new_data_path = "data/processed_data/preprocessed_current_data.csv"

    # Load new preprocessed data
    new_data = load_data(new_data_path)

    # Define features and target
    features = ['PriceChange', 'SMA_5', 'SMA_20', 'BollingerUpper', 'BollingerLower']
    target = 'Close'

    # Define X_new, y_new
    X_new = new_data[features]
    y_new = new_data[target]

    # Load the trained model
    model = create_model()
    model = joblib.load("models/saved_models/trained_model.pkl")

    # Update the model
    updated_model = update_model(model, X_new, y_new)

    # Save the updated model
    joblib.dump(updated_model, "models/saved_models/updated_model.pkl")
