import json
import requests

s = requests.Session()

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': '5F9D749B65CD44479C1BA2AA21991925',
    'Accept': '*',
    'X-Debug': '1',
    'User-Agent': 'FootPatrol/2.0 CFNetwork/808.2.16 Darwin/16.3.0',
    'Accept-Encoding': 'gzip, deflate',
    'MESH-Commcerce-Channel': 'iphone-app'
}

with open("config.json") as jsons:
    config = json.load(jsons)

req = s.post("https://commerce.mesh.mx/stores/footpatrol/customers", headers=headers, json=config)
if "error" in req.text:
    print(req.text)
else:
    print("Created succesfully")
