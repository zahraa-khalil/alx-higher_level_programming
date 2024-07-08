#!/usr/bin/python3
"""script to fetch data from URL"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(url, auth=HTTPBasicAuth(username, password))
    # print(response.json().get('id'))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print(None)
