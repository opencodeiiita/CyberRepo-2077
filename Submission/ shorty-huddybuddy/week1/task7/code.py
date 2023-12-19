import os 


def hidden(directory):
	hid_file = [f for f in os.listdir(directory) if f.startswith('.')]
	
	
	if not hid_file:
		print("NO")
		
	else :
		print("hidden")
		for files in hid_file:
			print(files)
			
			
if __name__=="__main__":
	path = input("enter directory path:")
	
	if not os.path.exists(path):
		print("invalid")
		
	else :
		hidden(path)
		
