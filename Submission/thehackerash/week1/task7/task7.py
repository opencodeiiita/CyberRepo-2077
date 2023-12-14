import os
#printing the names of all the hidden files in the current directory

def list_hidden_files(directory):
    files = os.listdir(directory)

    hidden_files = [file for file in files if file.startswith('.')]

    print("Hidden Files in {}: {}".format(directory, hidden_files))

if __name__ == "__main__":

    directory_path = "."  
    list_hidden_files(directory_path)
