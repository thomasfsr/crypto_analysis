from dotenv import load_dotenv
import coinmarketcapapi
import os

load_dotenv()

api_key = os.getenv('api_key')

cmc_client = coinmarketcapapi.CoinMarketCapAPI(api_key)
response = cmc_client.cryptocurrency_listings_latest()
print(response.data)


