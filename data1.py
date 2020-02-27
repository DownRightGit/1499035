import requests

resp = requests.get("https://data.melbourne.vic.gov.au/resource/9cnt-rnic.json")

data = resp.json()

for i in data:
   nm = i.get("geography")
   print(nm)