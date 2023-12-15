import os

directory = "/home/kali/Desktop"

files = os.listdir(directory)
hidden_files = [file for file in files if file.startswith('.')]
if hidden_files:
    print("Hidden files in the directory:")
    for hidden_file in hidden_files:
        print(hidden_file)
else:
    print("No hidden files found in the directory.")

