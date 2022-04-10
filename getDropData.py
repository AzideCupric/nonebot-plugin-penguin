import requests
import json


def getDropDate(itemId: str, url: str = 'https://penguin-stats.io/PenguinStats/api/v2/result/matrix', fileDir: str = "./db/dropItem.json") -> str:
    param = {'itemFilter': str(itemId)}
    response = requests.get(url=url, params=param)
    #print(response.url, response.status_code, sep='\n')
    raw_data = json.loads(response.content)
    data = raw_data['matrix']
    with open(fileDir, 'w', encoding='UTF-8') as wr:
        json.dump(data, wr, indent=4)
    return response.status_code
