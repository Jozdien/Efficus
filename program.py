import json
import math
import time

'''
This function's purpose is to extract the individual words, while accounting for the problems posed by punctuations: 
"I'm" is extracted as a single word, but the sentence "He said, "I'm a sentence"." is split into 9 words - ["He", "said", ",", """, "I'm", "a", "sentence", """, "."]
as "I'm" would be recognizable as a word in a dictionary, but "said," would not be, unless the dictionary was much more massive.
'''
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
original = f.read()
original = (original.lower()).replace('\n', " ")
words = separate(original)[:-1]
final = ""
no = 65408  # This is the integer number for the bit position at which unique words can be added.
counter = 0
new_words = 0
original_length = len(original) * 8.0
start_time = time.time()

with open('dictionary_wtn.json', 'r') as openfile: 
    dictionary_wtn = json.load(openfile)
with open('dictionary_ntw.json', 'r') as openfile:
	dictionary_ntw = json.load(openfile)

for a in range(10):
	new_time = time.time()
	for i in words:
		if(unicode(i, 'utf-8').isnumeric()):
			if(int(i) > 24107):  # The limit of the numbers directly stored in the dictionary
				for j in range(0, len(i), 4):
					if i[j] == "0":
						for k in i:
							final = final + dictionary_wtn[k]
					else: 
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
				new_words = new_words + 1
				dictionary_ntw[str(bin(no)[2:])] = i
				dictionary_wtn[i] = str(bin(no)[2:])
				no = no + 1
				final = final + dictionary_wtn[i]
		counter = counter + 1
	final = final[:-1]

	output_file = open('compressed.txt', 'w+')
	output_file.write(final)

	compressed_length = len(final)
	compression_factor = original_length / compressed_length

	#print(new_words)
	#print final
	print "Original length:",original_length
	print "Compressed length:",compressed_length
	print "Compression Factor:",compression_factor
	print "Time:",(time.time() - new_time)
	final = ""

print "Average Compression Time:",(time.time() - start_time)/10