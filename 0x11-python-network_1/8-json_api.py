#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}

    r = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        response = r.json()
        if len(response) == 0:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except:
        print("Not a valid JSON")
