import json
from collections import OrderedDict

f = open("words_unformatted.txt", "r")
dict_ntw = {}
dict_wtn = {}
first_tier = ['', '.', ',', '?', '\'', '\"']
second_tier = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  
				'(', ')', '+', '-', '*', ';', ':', "!", "$", "%", "&", "/"]
offset = 0
number = 10

for i in first_tier:
	no = str(bin(offset)[2:])
	dict_ntw[no] = i
	dict_wtn[i] = no
	offset = offset + 1
for i in f:
	i = i.lower()
	temp = i.split()[:2]
	no = str(bin(offset)[2:])
	if(no == "1000000"):
		for j in second_tier:
			no = str(bin(offset)[2:])
			dict_ntw[no] = j
			dict_wtn[j] = no
			offset = offset + 1
	dict_ntw[no] = temp[1]
	dict_wtn[temp[1]] = no
	offset = offset + 1
while str(bin(offset)[2:]) != "1111111110000000":
	no = str(bin(offset)[2:])
	dict_ntw[no] = str(number)
	dict_wtn[str(number)] = no
	number = number + 1
	offset = offset + 1

f.close()

json_ntw = json.dumps(OrderedDict(sorted(dict_ntw.items(), key=lambda kv: int(kv[0]))), indent = 4)
json_wtn = json.dumps(OrderedDict(sorted(dict_wtn.items(), key=lambda kv: int(kv[1]))), indent = 4)

with open("dictionary_wtn.json", "w+") as outfile: 
    outfile.write(json_wtn)
with open("dictionary_ntw.json", "w+") as outfile:
	outfile.write(json_ntw)