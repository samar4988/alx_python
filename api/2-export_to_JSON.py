#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""

import json
import requests
import sys

def get_employee_data(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Construct the URLs for employee details and TODO list
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee details
    try:
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching employee details: {e}")
        sys.exit(1)

    # Fetch TODO list
    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todo_data = response.json()
    except requests.exceptions.RequestException as e:        
        print(f"Error fetching TODO list: {e}")
        sys.exit(1)

    return employee_data, todo_data

def export_todo_progress_to_json(employee_data, todo_data, employee_id):
    # Extract relevant information
    employee_name = employee_data.get("name")
    tasks = []

    for task in todo_data:
        tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_data["username"]
        })

    # Create the JSON data
    json_data = {
        str(employee_id): tasks
    }

    # Write the JSON data to a file
    file_name = f"{employee_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {file_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_and_export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = get_employee_data(employee_id)
    export_todo_progress_to_json(employee_data, todo_data, employee_id)
