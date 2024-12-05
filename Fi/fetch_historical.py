import yfinance as yf

# Specify the ticker symbol for SoFi
ticker = "SOFI"

# Define the start and end dates for the desired historical data
start_date = "2019-01-01"
end_date = "2023-12-31"

# Download the historical data
data = yf.download(ticker, start=start_date, end=end_date)

# Print the first 5 rows of the data
print(data.head())

# You can save the data to a CSV file
# data.to_csv("SOFI_historical_data.csv")
