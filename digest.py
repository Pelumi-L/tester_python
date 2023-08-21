import requests
import json
data = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
responses = data.json()['data']
for response in responses:
    Nation = print(response['Nation'])
    NationID = print(response['ID Nation'])
    Year = print(response['Year'])
    Population = print(response['Population'])
# print(data.json()["data"][0]["ID Year"])