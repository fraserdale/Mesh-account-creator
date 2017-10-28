import json
import requests
import random
from random import randint
import string

s = requests.Session()
file = open("FPaccounts.txt","a+")
num_of_accounts = input("How many accounts?  ")
password_option = input("Type 1 to use password in config.json, type 2 to use random passwords:  ")

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

email = config['email']

index = config['email'].find("@")
for n in range(0,int(num_of_accounts)):
        if index == -1:
            account = str(randint(100000, 999999)) +"@" + email
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            file.writelines(account + "," + config['password'] + "\n")
            print(account + "," + config['password'])
            config['email'] = account
            print(config)
            req = s.post("https://commerce.mesh.mx/stores/footpatrol/customers", headers=headers, json=config)
            if req == "<Response [201]>":
                print("Created succesfully: " + account + "," + config['password'])
            else:
                print(account + "," + config['password'] + req.text)
        elif index == 0:
            account = str(randint(100000, 999999)) + email
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            file.writelines(account + "," + config['password'] + "\n")
            print(account + "," + config['password'])
            config['email'] = account
            print(config)
            req = s.post("https://commerce.mesh.mx/stores/footpatrol/customers", headers=headers, json=config)
            if req == "<Response [201]>":
                print("Created succesfully: " + account + "," + config['password'])
            else:
                print(account + "," + config['password'] + req.text)
        else:
            account = email[:index] + "+" + str(randint(100000, 999999)) + email[index:]
            if password_option == "2":
               config['password'] = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
            file.writelines(account + "," + config['password'] + "\n")
            print(account + "," + config['password'])
            config['email'] = account
            print(config)
            req = s.post("https://commerce.mesh.mx/stores/footpatrol/customers", headers=headers, json=config)
            if req == "<Response [201]>":
                print("Created succesfully: " + account + "," + config['password'])
            else:
                print(account + "," + config['password'] + req.text)
