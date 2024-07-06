#!/usr/bin/python3
"""script to fetch data from URL"""
import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print(f"Body response:")
        print(f"   - type: {type(html)}")
        print(f"   - content: {html}")
        print(f"   - utf8 content: {html.decode('utf-8')}")
