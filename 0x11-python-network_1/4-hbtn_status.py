#!/usr/bin/python3
"""Fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
