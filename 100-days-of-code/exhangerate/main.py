API_key = "b84ec73e3c8d5bc6bb471a88"
API_ENDPOINT = "https://v6.exchangerate-api.com/v6/b84ec73e3c8d5bc6bb471a88/latest/USD"

import requests

response = requests.get(API_ENDPOINT)
data = response.json()
rates = data["conversion_rates"]
print(data)



