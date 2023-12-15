import requests

url = "https://v6.exchangerate-api.com/v6/ff91783be3d5ef9d16f50c11/latest/USD"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)