import yfinance as yf
import pandas as pd
from sklearn.preprocessing import StandardScaler
from scripts.data_collection import fetch_current_data, fetch_historical_data
from scripts.data_preprocessing import preprocess_data
import os

if __name__ == "__main__":
    stock_symbols = ["AAPL", "MSFT", "JNJ", "JPM", "PG", "GOOGL", "AMZN", "KO", "PFE", "XOM"]
    historical_start_date = (pd.Timestamp.today() - pd.DateOffset(days=729)).strftime('%Y-%m-%d')
    historical_end_date = (pd.Timestamp.today() - pd.DateOffset(days=31)).strftime('%Y-%m-%d')
    current_start_date = (pd.Timestamp.today() - pd.DateOffset(days=30)).strftime('%Y-%m-%d')
    interval = "1h"

    os.makedirs("raw_data", exist_ok=True)
    os.makedirs("processed_data", exist_ok=True)

    # Fetch historical data
    historical_data = fetch_historical_data(stock_symbols, historical_start_date, historical_end_date, interval)
    historical_data.to_csv("raw_data/historical_data.csv")

    # Fetch current data
    current_data = fetch_current_data(stock_symbols, current_start_date, interval)
    current_data.to_csv("raw_data/current_data.csv")

    # Load and preprocess data
    historical_data_path = "raw_data/historical_data.csv"
    current_data_path = "raw_data/current_data.csv"

    # Load data
    historical_data = pd.read_csv(historical_data_path)
    current_data = pd.read_csv(current_data_path)

    # Preprocess data
    preprocessed_historical_data = preprocess_data(historical_data)
    preprocessed_current_data = preprocess_data(current_data)
    
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
    
    # Save preprocessed data
    scaled_historical_data.to_csv("processed_data/preprocessed_historical_data.csv")
    scaled_current_data.to_csv("processed_data/preprocessed_current_data.csv")
