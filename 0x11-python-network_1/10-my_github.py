#!/usr/bin/python3
"""script to fetch data from URL"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
