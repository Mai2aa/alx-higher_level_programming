#!/usr/bin/python3
""" list 10 commits from the repository rails"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = "https://developer.github.com/v3/repos/{}/{}/commits/".format(
            repo_name, owner_name)
    response = requests.get(url)
    commits = response.json()
    for commit in commits[:10]:
        sha = commit["sha"]
        auth_name = commit["commit"]["author"]["name"]
        print("{}: {}".format(sha, auth_name))
