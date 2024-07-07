#!/usr/bin/python3
"""script to fetch data from URL and handle error"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
