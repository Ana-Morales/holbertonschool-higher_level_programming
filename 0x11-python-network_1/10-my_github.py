#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses the
Github API to display your id"""

if __name__ == "__main__":
    import requests
    import sys

    user = sys.argv[1]
    psw = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(user, psw))
    print(r.json().get("id"))
