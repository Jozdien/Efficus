import re
import json

def separate(s):
	s_arr = s.split()
	arr = []
	flag = 0
	chars = ['\'', '\"', '.', ',', '(', ')', '+', '/', '-', '*', ':', ';', '!', '$', '%', '&']
	for i in s_arr:
		for char in chars:
			if char in i:
				index = i.index(char)
				if(index == 0 or index == len(i) - 1):
					j = i.split(char)
					arr.append(j[0])
					arr.append(j[1])
					flag = 1
		if flag == 0:
			arr.append(i)
		flag = 0
	return arr

original = "Here's to us."
original = original.lower()
words = separate(original)[:-1]
final = ""
no = 65408

with open('dictionary_wtn.json', 'r') as openfile: 
    dictionary_wtn = json.load(openfile)

for i in words:
	if(unicode(i, 'utf-8').isnumeric()):
		if(int(i) > 24107):
			for j in range(0, len(line), 4):
				final = final + dictionary_wtn[i[j:j+4]]
			final = final + "\n"
		else:
			final = final + dictionary_wtn[i]
	else:
		if(i in dictionary_wtn):
			final = final + dictionary_wtn[i] + "\n"
		else:
			dictionary_ntw[str(bin(no)[2:])] = i
			dictionary_wtn[i] = str(bin(no)[2:])
			no = no + 1
			final = final + dictionary_wtn[i] + "\n"
final = final[:-1]

print(final)