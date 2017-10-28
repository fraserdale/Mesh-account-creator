import json
import requests

s = requests.Session()

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': 'EA0E72B099914EB3BA6BE90A21EA43A9',
    'Accept': '*',
    'X-Debug': '1',
    'User-Agent': 'Size/5.3.1.207 CFNetwork/808.3 Darwin/16.3.0',
    'Accept-Encoding': 'gzip, deflate',
    'MESH-Commcerce-Channel': 'iphone-app'
}

with open("config.json") as jsons:
    config = json.load(jsons)

req = s.post("https://commerce.mesh.mx/stores/size/customers", headers=headers, json=config)
print(req.text)