#!/usr/bin/python3
"""Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display"""


import sys
"""Importing sys Package"""

import requests
"""Importing request package"""

def get_github_id(username, token):
    """
    Fetches the GitHub user ID using Basic Authentication with a personal access token.

    Args:
        username (str): GitHub username.
        token (str): Personal access token for authentication.

    Returns:
        None: Prints the GitHub user ID or an error message.
    """
    url = "https://api.github.com/user"
    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get("id"))
        elif response.status_code == 401:
            print("None")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]

    get_github_id(username, token)