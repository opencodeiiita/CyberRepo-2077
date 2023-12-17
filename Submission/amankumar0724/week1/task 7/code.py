import os
def printHiddenFiles(directory):
    files = os.listdir(directory)
    hid_files = [file for file in files if file.startswith('.')]
    c=0
    for hid_file in hid_files:
        c=c+1
        print(hid_file)
    print(f"Number of hidden files are:",c)

if __name__ =="__main__":
    directory = os.getcwd()
    print(f"Hidden files in {directory}:")
    printHiddenFiles(directory)