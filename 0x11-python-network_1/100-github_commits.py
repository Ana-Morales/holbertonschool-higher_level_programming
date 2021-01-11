#!/usr/bin/python3
"""Takes your Github credentials (username and password) and uses the
Github API to display your id"""

if __name__ == "__main__":
    import requests
    import sys

    own = sys.argv[2]
    rep = sys.argv[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(own, rep)
    r = requests.get(url)
    try:
        com = r.json()
        for commit in com[:10]:
            print("{}: {}".format(commit.get("sha"),
                                  commit.get("commit").
                                  get("author").get("name")))
    except:
        print("Error")
