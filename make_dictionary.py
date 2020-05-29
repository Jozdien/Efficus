'''
import json
f = open('words_dictionary.json')
data = json.load(f)
index = "0" # 19-digit binary code, large enough for everything
dictionary_ntw = []  #Store numbers, special characters too
dictionary_wtn = []
'''

#f = open("words_unformatted.txt", "r")
f = open("text.txt", "r")
arr = []
for i in f:
	arr.append(i.split())