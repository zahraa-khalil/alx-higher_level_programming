#!/usr/bin/python3
"""script to fetch data from URL"""
import requests


url = 'https://alx-intranet.hbtn.io/status'
res = requests.get(url)
print(f"Body response:")
print(f"\t- type: {type(res.text)}")
print(f"\t- content: {res.text}")
