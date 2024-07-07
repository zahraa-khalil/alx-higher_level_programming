#!/usr/bin/python3
"""script to fetch data from URL"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    emailObj = {'email': email}
    encoded_email = urllib.parse.urlencode(emailObj).encode('ascii')
    request = urllib.request.Request(url, encoded_email)
    with urllib.request.urlopen(request) as response:
        response_data = response.read().decode('utf-8')
        print(response_data)
