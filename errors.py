#! usr/bin/env python3

import sys

try:
    names = open("names.txt").readlines()
except FileNotFoundError as e:
    print(f"{str(e)}")
    sys.exit(1)

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)