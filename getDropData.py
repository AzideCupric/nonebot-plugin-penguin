import requests
import json

url = 'https://penguin-stats.io/PenguinStats/api/v2/result/matrix'
param = {'itemFilter': '30083'}
response = requests.get(url=url, params=param)
print(response.url, response.status_code, sep='\n')
raw_data = json.loads(response.content)
data = raw_data['matrix']
with open("./db/dropItem.json", 'w', encoding='UTF-8') as wr:
    json.dump(data, wr, indent=4)
