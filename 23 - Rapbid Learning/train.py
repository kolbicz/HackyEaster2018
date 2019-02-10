import requests
import json

line=''

with open('train.txt', 'a') as f:
	r = requests.get('http://whale.hacking-lab.com:2222/train')
	jsonObject = json.loads(r.text)
	for key in jsonObject:
		line+=str(key)+','
	f.write(line[:-1]+'\n')

with open('train.txt', 'a') as f:
		for i in range(150):
			line=''
			r = requests.get('http://whale.hacking-lab.com:2222/train')
			jsonObject = json.loads(r.text)
			for key in jsonObject:
				value = jsonObject[key]
				line+=str(value)+','
			f.write(line[:-1]+'\n')