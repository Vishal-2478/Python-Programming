# WAP that computes total size of all files
# file_size.py

import os

filename = input("Enter filename (with path if needed): ")

try:
    size = os.path.getsize(filename)
    print(f"\nSize of '{filename}' = {size} bytes")
except FileNotFoundError:
    print(f"\nFile '{filename}' not found!")
