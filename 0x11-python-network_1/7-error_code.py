#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the body of the
response."""

if __name__ == "__main__":

    import requests
    import sys

    r = requests.get(sys.argv[1])
    code = r.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
