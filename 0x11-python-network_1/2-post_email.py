#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
(decoded in utf-8)"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    email = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    req = urllib.request.Request(sys.argv[1], email)
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
