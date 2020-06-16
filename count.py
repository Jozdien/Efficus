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

f = open("book.txt", 'r')
original = f.read()
original = original.lower()
words = separate(original)[:-1]

no_of_words = len(words) * 1.0
no_of_characters = len(original) * 1.0
avg_length = no_of_characters/no_of_words

print "Number of words:",no_of_words
print "Number of characters:",no_of_characters
print "Average word length:",avg_length