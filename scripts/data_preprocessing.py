import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    # Load CSV data
    data = pd.read_csv(file_path)

    return data

def preprocess_data(data):
    # Fill missing values using forward fill
    data = data.ffill()

    # Calculate additional features
    data['PriceChange'] = data['Close'].diff()
    # data['HourOfDay'] = data.index.dt.hour
    # data['DayOfWeek'] = data.index.dayofweek
    
    data['SMA_5'] = data['Close'].rolling(window=5).mean()
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['BollingerUpper'] = data['SMA_20'] + 2 * data['Close'].rolling(window=20).std()
    data['BollingerLower'] = data['SMA_20'] - 2 * data['Close'].rolling(window=20).std()

    return data

if __name__ == "__main__":
    historical_data_path = "data/raw_data/historical_data.csv"
    current_data_path = "data/raw_data/current_data.csv"

    # Load data
    historical_data = load_data(historical_data_path)
    current_data = load_data(current_data_path)

    # Preprocess data
    preprocessed_historical_data = preprocess_data(historical_data)
    preprocessed_current_data = preprocess_data(current_data)
    historical_col_datetime = preprocessed_historical_data["Datetime"]
    current_col_datetime = preprocessed_current_data["Datetime"]
    # Exclude non-numeric columns before scaling
    columns_to_scale = preprocessed_historical_data.select_dtypes(include=[float]).columns

    # Normalize features using StandardScaler
    scaler = StandardScaler()
    scaled_historical_data = pd.DataFrame(scaler.fit_transform(preprocessed_historical_data[columns_to_scale]),
                                          columns=columns_to_scale,
                                          index=preprocessed_historical_data.index)
    scaled_current_data = pd.DataFrame(scaler.transform(preprocessed_current_data[columns_to_scale]),
                                       columns=columns_to_scale,
                                       index=preprocessed_current_data.index)
    scaled_historical_data["Datetime"] = historical_col_datetime
    scaled_current_data["Datetime"] = current_col_datetime
    # Save preprocessed data
    scaled_historical_data.to_csv("data/processed_data/preprocessed_historical_data.csv")
    scaled_current_data.to_csv("data/processed_data/preprocessed_current_data.csv")
