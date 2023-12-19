import os
directory = os.getcwd()
print(directory)

files = os.listdir(directory)
for f in files:
  if (f.startswith(".")):
    print("I found a hidden file/dir called " + f)
                       
