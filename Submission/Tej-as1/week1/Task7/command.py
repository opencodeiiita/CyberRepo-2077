import os
def hidden(filename):
    name = os.path.basename(os.path.abspath(filename))
    return name.startswith('.')
for filename in os.listdir():
    if(hidden(filename)):
        print(filename)
