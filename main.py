import requests

url = "https://streamlabs.com/api/v2.0/donations"

headers = {
    "accept": "application/json",
    "Bearer": "<access_token>"
}

response = requests.get(url, headers=headers)

print(response.text)