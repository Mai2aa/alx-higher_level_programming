#!/usr/bin/python3
""" list 10 commits from the repository rails"""
import requests
import sys


if __name__ == "__main__":
    url = "https://developer.github.com/v3/repos/commits/"
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    params = {"per_page": 10}
    response = requests.get(url, params=params)
    commits = response.json()
    for commit in commits:
        sha = commit["sha"]
        auth_name = commit["author"]["name"]
        print("{}: {}".format(sha, auth_name))
