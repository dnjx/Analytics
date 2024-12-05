import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Specify the ticker symbol for SoFi
ticker = "SOFI"

# Define the start and end dates for the desired historical data
start_date = "2021-06-04"
end_date = "2024-11-15"

# Download the historical data
data = yf.download(ticker, start=start_date, end=end_date)

# Print the first 5 rows of the data
print(data.head())

# You can save the data to a CSV file
# data.to_csv("SOFI_historical_data.csv")
# print(data.all)

# Prepare data
X = data[['Open', 'High', 'Low', 'Volume']]
y = data['Close']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Prepare input data for forecasting (last 30 days)
last_30_days = X[-30:]

# Make predictions for the next month (30 days)
future_predictions = model.predict(last_30_days)

print(future_predictions)