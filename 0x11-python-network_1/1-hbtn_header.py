#!/usr/bin/python3
"""script to fetch data from URL"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        id = headers.get('X-Request-Id')
        print(id)
