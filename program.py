words = re.split(r'(\W+)', original) # Split, separate special characters
final = ""
for i in words:
	final = final + dictionary_wtn[i] + " "
print(final)