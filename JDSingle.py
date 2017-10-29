import json
import requests

s = requests.Session()

headers = {
    'Content-Type': 'application/json',
    'X-API-Key': '1A17CC86AC974C8D9047262E77A825A4',
    'Accept': '*',
    'X-Debug': '1',
    'User-Agent': 'JDSports/5.3.1.207 CFNetwork/808.3 Darwin/16.3.0',
    'Accept-Encoding': 'gzip, deflate',
    'MESH-Commcerce-Channel': 'iphone-app'
}

with open("config.json") as jsons:
    config = json.load(jsons)

req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
if "error" in req.text:
    print(req.text)
else:
    print("Created succesfully")
