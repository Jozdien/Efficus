import re
import json

original = "you I to"
words = re.findall(r"[\w]+|[^\s\w]", original) # Split, separate special characters
final = ""

with open('dictionary_wtn.json', 'r') as openfile: 
    dictionary_wtn = json.load(openfile)

for i in words:
	final = final + dictionary_wtn[i] + "\n"
final = final[:-1]

print(final)