#!/usr/bin/python3
"""Python script that takes in a URL and an email address, sends a POST request"""


import sys
"""Importing sys package"""

import requests
"""importing request package"""

def send_post_request(url, email):
    # Data to be sent in the POST request
    data = {'email': email}

    try:
        # Send a POST request to the URL with the email parameter
        response = requests.post(url, data=data)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Display the response body
            print(response.text)
        else:
            # Display an error message if the status code is not 200
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if the script is run with the correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <url> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request and display the response
    send_post_request(url, email)