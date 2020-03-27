import requests, json

req = requests.get(url='https://www.mtgjson.com/files/StandardPrintings.json')

data = req.json()

#---------this saves the data to a file-----------
with open('data.json', 'w') as f:
    json.dump(data, f)