import os

for file in os.listdir():
    if file.startswith("."):
        print(file)
