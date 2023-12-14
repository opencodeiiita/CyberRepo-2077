import os

def hidden_files(directory):
	hidden = [f for f in os.listdir(directory) if f.startswith('.')]
	for file in hidden:
		print(file)

if __name__ == "__main__":
	target_dir = '/root/Desktop'
	print("Hidden files in", target_dir, "are :")
	hidden_files(target_dir)
