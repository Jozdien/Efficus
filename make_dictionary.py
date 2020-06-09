import json
from collections import OrderedDict

'''
f = open('words_dictionary.json')
data = json.load(f)
index = "0" # 19-digit binary code, large enough for everything
dictionary_ntw = []  #Store numbers, special characters too
dictionary_wtn = []
'''

f = open("words_unformatted.txt", "r")
dict_ntw = {}
dict_wtn = {}
for i in f:
	temp = i.split()[:2]
	dict_ntw[temp[0]] = temp[1]
	dict_wtn[temp[1]] = temp[0]
f.close()

json_ntw = json.dumps(OrderedDict(sorted(dict_ntw.items(), key=lambda kv: int(kv[0]))), indent = 4)
json_wtn = json.dumps(OrderedDict(sorted(dict_wtn.items(), key=lambda kv: int(kv[1]))), indent = 4)

with open("dictionary_wtn.json", "w+") as outfile: 
    outfile.write(json_ntw)
with open("dictionary_ntw.json", "w+") as outfile:
	outfile.write(json_wtn)