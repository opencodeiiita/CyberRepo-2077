import os

dt = "/home/kali/Desktop/task7"

files = os.listdir(dt)

hidden_files = [file for file in files if file.startswith('.')]

if hidden_files:

    print("Hidden files in the directory:")
    for file in hidden_files:
        print(file)

else:
    print("Hidden files Not in directory.")


