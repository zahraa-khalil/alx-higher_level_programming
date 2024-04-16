#!/usr/bin/python3

def read_file(filename=""):
    with open(filename , "r", encoding="UTF8") as f:
        content = f.read()
        print(content)
