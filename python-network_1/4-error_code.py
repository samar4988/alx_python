#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL and displays the body"""


import sys
"""importing sys package"""

import requests
"""Importing request package"""

def fetch_url(url):
    try:
        # Send a GET request to the provided URL
        response = requests.get(url)
        
        # Display the body of the response
        print(response.text)

        # Check if the response status code is greater than or equal to 400
        if response.status_code >= 400:
            # Print an error message with the HTTP status code
            print(f"Error code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    # Call the function to send the request and display the response
    fetch_url(url)