import os
def list_hidden_files():
    current_directory = os.getcwd()
    hidden_files = [file for file in os.listdir(current_directory) if file.startswith('.')]
    for file in hidden_files:
        print(file)
list_hidden_files()