import yfinance as yf
from datetime import datetime
import pandas as pd

# Specify the ticker symbol for the S&P 500 index (^GSPC)
sp500_symbol = '^GSPC'

# Specify the ticker symbol for Bitcoin (BTC-USD)
bitcoin_symbol = 'BTC-USD'

# Specify the start date
start_date = '2021-01-01'

# Get the current date and format it as 'YYYY-MM-DD'
end_date = datetime.now().strftime('%Y-%m-%d')

# Retrieve historical price data for the S&P 500 index
sp500_data = yf.download(sp500_symbol, start=start_date, end=end_date)

# Calculate the average closing price for each day for S&P 500
average_sp500_prices = sp500_data['Close'].resample('D').mean().rename("S&P 500")

# Retrieve historical price data for Bitcoin
bitcoin_data = yf.download(bitcoin_symbol, start=start_date, end=end_date)

# Calculate the average closing price for each day for Bitcoin
average_bitcoin_prices = bitcoin_data['Close'].resample('D').mean().rename("Bitcoin")
average_sp500_prices = pd.DataFrame(average_sp500_prices)

# Merge the two datasets based on their index (date)
merged_data = average_sp500_prices.merge(average_bitcoin_prices,how = 'left', left_index=True, right_index=True)
merged_clean_data = merged_data.dropna()
# Print the merged dataset
print(merged_clean_data)
print(merged_clean_data.info())
print(merged_clean_data.describe())