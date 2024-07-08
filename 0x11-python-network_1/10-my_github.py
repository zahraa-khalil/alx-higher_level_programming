#!/usr/bin/python3
"""script to fetch data from URL"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(None)
