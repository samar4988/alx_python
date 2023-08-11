#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user"""


import sys
"""Importing sys package"""

import requests
"""Importing request package"""

def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    
    try:
        # Send a POST request to the URL with the letter parameter
        response = requests.post(url, data=data)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            try:
                # Try to parse the JSON content of the response
                json_data = response.json()
                
                # Check if JSON is not empty and has 'id' and 'name' keys
                if json_data and 'id' in json_data and 'name' in json_data:
                    # Display the id and name
                    print(f"[{json_data['id']}] {json_data['name']}")
                else:
                    # Display No result if the JSON is empty or lacks required keys
                    print("No result")
            except ValueError:
                # Display Not a valid JSON if the JSON is invalid
                print("Not a valid JSON")
        else:
            # Display an error message if the status code is not 200
            print(f"Error: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        # If no argument is given, set q="" as required
        search_user("")
    else:
        letter = sys.argv[1]
        search_user(letter)