from dotenv import load_dotenv
from coinmarketcapapi import CoinMarketCapAPI
import os

load_dotenv()

api_key = os.getenv('api_key')

cmc_client = CoinMarketCapAPI(api_key)
response = cmc_client.cryptocurrency_listings_latest()
print(response.data)