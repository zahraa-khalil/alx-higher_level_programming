#!/usr/bin/python3
"""script to fetch data from URL"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) == 2 else ""
    letterObj = {'q': q}
    res = requests.post(url, data=letterObj)
    try:
        res = res.json()
        if res == {}:
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except ValueError:
        print("Not a valid JSON")
