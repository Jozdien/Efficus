import json
from collections import OrderedDict

f = open("words_unformatted.txt", "r")
dict_ntw = {"0": ".", "1": ",", "10": "'", "11": "\"", "110110": "0", "110111": "1", "111000": "2", "111001": "3", "111010": "4", "111011": "5", "111100": "6", "111101": "7", "111110": "8", "111111": "9", "1000000": "(", "1000001": ")", "1000010": "+", "1000011": "-", "1000100": "*", "1000101": ";", "1000110": ":", "1000111": "!", "1001000": "$", "1001001": "%", "1001010": "&", "1001011": "/"}
dict_wtn = {}
#TODO: Fill out the remaining bits with that many digits in the JSON with numbers

for i in f:
	temp = i.split()[:2]
	dict_ntw[str(bin(int(temp[0]))[2:])] = temp[1]
	dict_wtn[temp[1]] = str(bin(int(temp[0]))[2:])
f.close()

json_ntw = json.dumps(OrderedDict(sorted(dict_ntw.items(), key=lambda kv: int(kv[0]))), indent = 4)
json_wtn = json.dumps(OrderedDict(sorted(dict_wtn.items(), key=lambda kv: int(kv[1]))), indent = 4)

with open("dictionary_wtn.json", "w+") as outfile: 
    outfile.write(json_wtn)
with open("dictionary_ntw.json", "w+") as outfile:
	outfile.write(json_ntw)