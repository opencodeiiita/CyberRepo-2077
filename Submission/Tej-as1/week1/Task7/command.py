import os
def hidden(file):
	name = os.path.basename(os.path.abspath(file))
	return name.startswith('.')
for file in os.listdir():
	if(hidden(file)):
		print(file)