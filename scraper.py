import requests
import json

url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=20&collection=genesis-creepz&order_by=sale_price"
headers = {"Accept": "application/json"}
response = requests.request("GET", url, headers=headers)
print(response)

# pretty_json = json.loads(response.text)
# print(json.dumps(pretty_json,indent=2))
# print(type(response))


