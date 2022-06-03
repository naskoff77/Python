# Script that pulls current price data for all cryptocurrency on coinbase pro
from numpy import row_stack
import requests
import pandas

# open coinbase API for product information
REST_API_URL = 'https://api.pro.coinbase.com/products'

# get results from API
response = requests.get(REST_API_URL)
response_content = response.content
response_text = response.text
response_headers = response.headers

# set pandas row max to unlimited
pandas.set_option('display.max_rows', None)

# read json using pandas
currencies = pandas.read_json(response_text)

# print results
print("/nNumber of columns in dataframe: %i" % (currencies.shape[1]))
print("/nNumber of rows in dataframe: %i" % (currencies.shape[0]))

print(list(currencies.columns))
print()
currencies[['id', 'quote_currency', 'base_min_size', 'base_max_size']]