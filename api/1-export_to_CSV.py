#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress and exports it in CSV format.
"""

import pandas as pd
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

def export_to_csv(employee_data, todo_data):
    # Extract relevant information
    user_id = employee_data.get("id")
    username = employee_data.get("username")

    # Create a DataFrame for the TODO list
    todo_df = pd.DataFrame(todo_data)

    # Select relevant columns and add user-specific data
    todo_df = todo_df[["completed", "title"]]
    todo_df["user_id"] = user_id
    todo_df["username"] = username

    # Rename columns
    todo_df = todo_df.rename(columns={"completed": "TASK_COMPLETED_STATUS", "title": "TASK_TITLE"})

    # Save to CSV
    csv_filename = f"{user_id}.csv"
    todo_df.to_csv(csv_filename, index=False)
    print(f"Data exported to {csv_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2: