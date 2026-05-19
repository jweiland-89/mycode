#!/usr/bin/env python3

"""Attempt to read a file in the current directory"""

import os # Importing the os module for directory operations

def main():
    """Main Logic"""
    os.chdir("/tmp") # change the working directory to /tmp
    with open("protoss.txt", "r") as foo:
        print (foo.read())

main()
