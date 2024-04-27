#!/usr/bin/python3
""" takes GitHub credentials(username, password)GitHub API to display id"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    if response.status_code == 200:
        content = response.json()
        print(content["id"])
    else:
        print("None")
