import json
import math

def separate(s):
	s_arr = s.split(' ')
	arr = []
	flag = 0
	flag_two = 0
	flag_three = 0
	chars = ['\'', '\"', '.', ',', '?', '(', ')', '+', '/', '-', '*', ':', ';', '!', '$', '%', '&']
	for i in s_arr:
		for char in chars:
			if char in i:
				index = i.index(char)
				if(index == 0):
					j = i.split(char)
					arr.append(j[0].strip())
					i = j[1].strip()
					for char in chars:
						if char in i:
							index = i.index(char)
							if(index == 0):
								j = i.replace(char, "")
								arr.append(char)
								arr.append(j.strip())
								flag_two = 1
							elif(index == len(i) - 1):
								j = i.replace(char, "")
								arr.append(j.strip())
								arr.append(char)
								flag_two = 1
					if(flag_two == 0):
						arr.append(j[1].strip())
					flag_two = 0
					flag = 1
				elif(index == len(i) - 1):
					j = i.split(char)
					arr.append(j[1].strip())
					i = j[0].strip()
					for char in chars:
						if char in i:
							index = i.index(char)
							if(index == 0):
								j = i.replace(char, "")
								arr.append(char)
								arr.append(j.strip())
								flag_three = 1
							elif(index == len(i) - 1):
								j = i.replace(char, "")
								arr.append(j.strip())
								arr.append(char)
								flag_three = 1
					if(flag_three == 0):
						arr.append(j[0].strip())
					flag_three = 0
					flag = 1
		if flag == 0:
			arr.append(i.strip())
		flag = 0
	return arr

f = open("book.txt", 'rw')
original = f.read()[:10000].decode("utf-8").replace(u'\xe2\x80\x9d', '"').encode("utf-8")
original = (original.lower()).replace('\n', " ")
words = separate(original)[:-1]
final = ""
no = 65408
counter = 0
original_length = len(original) * 1.0

with open('dictionary_wtn.json', 'r') as openfile: 
    dictionary_wtn = json.load(openfile)
with open('dictionary_ntw.json', 'r') as openfile:
	dictionary_ntw = json.load(openfile)

for i in words:
	print(i)
	if(unicode(i, 'utf-8').isnumeric()):
		if(int(i) > 24107):
			for j in range(0, len(i), 4):
				final = final + dictionary_wtn[i[j:j+4]]
		elif i[0] == "0":
			for j in i:
				final = final + dictionary_wtn[j]
		elif len(i) == 2:
			for j in i:
				final = final + dictionary_wtn[j]
		else:
			final = final + dictionary_wtn[i]
	else:
		if(i in dictionary_wtn):
			final = final + dictionary_wtn[i]
		else:
			dictionary_ntw[str(bin(no)[2:])] = i
			dictionary_wtn[i] = str(bin(no)[2:])
			no = no + 1
			final = final + dictionary_wtn[i]
	counter = counter + 1
final = final[:-1]

compressed_length = math.ceil(len(final) / 8.0)
compression_factor = compressed_length / original_length

#print final
print "Original length:",original_length
print "Compressed length:",compressed_length
print "Compression Factor:",compression_factor