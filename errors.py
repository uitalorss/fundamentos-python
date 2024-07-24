#! usr/bin/env python3

import time

def open_file(filepath, retry=1):
    """Tries to open a file, if error, retries n times"""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readlines()
        except FileNotFoundError as e:
            print(f"{str(e)}")
            time.sleep(3)
    return []


for line in open_file("names.txt", retry=5):
    print(line)