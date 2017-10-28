import json
import requests
from random import randint

s = requests.Session()
file = open("JDaccounts.txt","a+")
num_of_accounts = input("How many account?")

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

for n in range(0,int(num_of_accounts)):
        index = config['email'].find("@")
        if index == -1:
            account = str(randint(100000, 999999)) +"@" + config['email']
            file.writelines(account + "," + config['password'] + "\n")
            print(account + "," + config['password'])
            req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
        elif index == 0:
            account = str(randint(100000, 999999)) + config['email']
            file.writelines(account + "," + config['password'] + "\n")
            print(account + "," + config['password'])
            req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
        else:
             account = config['email'][:index] + "+" + str(randint(100000, 999999)) + config['email'][index:]
             file.writelines(account + "," + config['password'] + "\n")
             print(account + "," + config['password'])
             req = s.post("https://commerce.mesh.mx/stores/jdsports/customers", headers=headers, json=config)
        #print(req.text) 