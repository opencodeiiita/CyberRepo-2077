import os

def is_hidden(file):
	return file.startswith(".")

for file in os.listdir():
	if (is_hidden(file)):
		print(file)
