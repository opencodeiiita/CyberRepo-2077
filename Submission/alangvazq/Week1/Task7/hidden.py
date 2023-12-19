import os

def print_hidden_files():

    all_files = os.listdir()

    only_hidden_files = [file for file in all_files if file.startswith('.')]
    for item in only_hidden_files:
        print(item)

if __name__ == "__main__":
    print_hidden_files()
