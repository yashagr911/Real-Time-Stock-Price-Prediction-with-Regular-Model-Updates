from django.shortcuts import render
from datetime import datetime
from sklearn.preprocessing import StandardScaler
import pandas as pd
import joblib

def predict_stock_prices(request):
    if request.method == 'POST':
        input_time = request.POST.get('input_time', '')
        
        # Parse the input time
        try:
            input_datetime = datetime.strptime(input_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return render(request, 'prediction_app/predict.html', {'error': 'Invalid time format'})

        # Load the trained model and scaler
        loaded_model = joblib.load("model/saved_models/trained_model.pkl")
        scaler = StandardScaler()  # Use the same scaler as during training
        
        # Preprocess user input
        user_input = pd.DataFrame({'Datetime': [input_datetime]})
    
       
        input_features_scaled = scaler.transform(user_input)
        
        # Make predictions for all stocks
        predicted_prices = loaded_model.predict(input_features_scaled)
        stock_symbols = ["AAPL", "MSFT", "JNJ", "JPM", "PG", "GOOGL", "AMZN", "KO", "PFE", "XOM"]
        stock_predictions = dict(zip(stock_symbols, predicted_prices))
        
        return render(request, 'prediction_app/predict.html', {'stock_predictions': stock_predictions})
    
    return render(request, 'prediction_app/predict.html', {})

def preprocess_data(data):
    # Implement your preprocessing logic here
    # This is just a placeholder
    return data

features = ['Datetime']  # Add other features as needed
