import requests
from pprint import pprint

URL = "https://api.npoint.io/5abcca6f4e39b4955965"

response = requests.get(URL)
pprint(response.json()[0]['body'])