from coinmarketcapapi import CoinMarketCapAPI

cmc_client = CoinMarketCapAPI()
response = cmc_client.cryptocurrency_listings_latest()
print(response.data)