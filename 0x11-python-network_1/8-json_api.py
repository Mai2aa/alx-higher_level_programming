#!/usr/bin/python3
""" Search API """
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q' : letter}
    response = requests.post(url, data=data)
    try:
        content = response.json()
        if content:
            print("[{}] {}".format(content["id"], content["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
