#!/usr/bin/python3
"""script to fetch data from URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    letter = sys.argv[2]
    emailObj = {'letter': letter}
    res = requests.post(url, emailObj)
    print(res.text)
