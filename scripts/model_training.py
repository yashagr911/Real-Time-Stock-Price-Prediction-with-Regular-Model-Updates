import pandas as pd
from sklearn.model_selection import train_test_split
from models.model_code.HistGradientBoostingRegressor  import create_model
import joblib

def load_data(file_path):
    data = pd.read_csv(file_path, parse_dates=['Datetime'])
    return data

def train_model(X_train, y_train):
    model = create_model()
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    historical_data_path = "data/processed_data/preprocessed_historical_data.csv"

    # Load preprocessed data
    historical_data = load_data(historical_data_path)

    # Define features and target
    features = ['PriceChange', 'SMA_5', 'SMA_20', 'BollingerUpper', 'BollingerLower']
    target = 'Close'

    # Split data into train and test sets
    train_data, _ = train_test_split(historical_data, test_size=0.2, random_state=42)

    # Define X_train, y_train
    X_train = train_data[features]
    y_train = train_data[target]

    # Train the model
    model = train_model(X_train, y_train)

    # Save the trained model
    joblib.dump(model, "models/saved_models/trained_model.pkl")
