#!/usr/bin/env python3

import os

cwd = os.getcwd()
files = os.listdir(cwd)
for file in files:
    if file.startswith('.'):
        print(file)