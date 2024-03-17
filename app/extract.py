import yfinance as yf
from datetime import datetime
import pandas as pd

sp500_symbol = '^GSPC'
bitcoin_symbol = 'BTC-USD'

start_date = '2011-01-01'
end_date = datetime.now().strftime('%Y-%m-%d')

sp500_data = yf.download(sp500_symbol, start=start_date, end=end_date)
average_sp500_prices = sp500_data['Close'].resample('D').mean().rename("S&P 500")

bitcoin_data = yf.download(bitcoin_symbol, start=start_date, end=end_date)
average_bitcoin_prices = bitcoin_data['Close'].resample('D').mean().rename("Bitcoin")

merged_data = pd.concat([average_sp500_prices, average_bitcoin_prices], axis=1, join='inner', ignore_index=True)
#merged_clean_data = merged_data.dropna()

print(merged_data)
print(merged_data.info())
print(merged_data.describe())