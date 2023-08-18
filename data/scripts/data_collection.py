import yfinance as yf
import pandas as pd
import datetime

def fetch_historical_data(symbols, start_date, end_date, interval):
    combined_data = pd.DataFrame()

    for symbol in symbols:
        stock_data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
        stock_data['Symbol'] = symbol
        combined_data = pd.concat([combined_data, stock_data])

    return combined_data

def fetch_current_data(symbols, start_date, interval):
    combined_data = pd.DataFrame()

    for symbol in symbols:
        stock_data = yf.download(symbol, start=start_date, interval=interval)
        stock_data['Symbol'] = symbol
        combined_data = pd.concat([combined_data, stock_data])

    return combined_data

if __name__ == "__main__":
    stock_symbols = ["AAPL", "MSFT", "JNJ", "JPM", "PG", "GOOGL", "AMZN", "KO", "PFE", "XOM"]
    today = pd.Timestamp.today().strftime('%Y-%m-%d')
    historical_end_date = (pd.Timestamp.today() - pd.DateOffset(days=31)).strftime('%Y-%m-%d')
    historical_start_date = (pd.Timestamp.today() - pd.DateOffset(days=729)).strftime('%Y-%m-%d')
    current_start_date = (pd.Timestamp.today() - pd.DateOffset(days=30)).strftime('%Y-%m-%d')
    interval = "1h"
    
    historical_data = fetch_historical_data(stock_symbols, historical_start_date, historical_end_date, interval)
    historical_data.to_csv("data/raw_data/historical_data.csv")

    current_data = fetch_current_data(stock_symbols, current_start_date, interval)
    current_data.to_csv("data/raw_data/current_data.csv")
