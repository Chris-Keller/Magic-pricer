import requests, json
req = requests.get(url='https://www.mtgjson.com/files/StandardPrintings.json')

data = req.json()

with open('data.json') as json_file: 
	data = json.load(json_file) 
	# Print the data of dictionary
	for x in range(0,len(data['ELD']['cards'])):
		print("\nCard name = ", data['ELD']['cards'][x]['name'])
		print("Card price = ", data['ELD']['cards'][x]['prices']['paper'])