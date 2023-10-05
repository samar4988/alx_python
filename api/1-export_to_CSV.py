#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""

import csv
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
    USER_ID = employee_data["id"]
    employee_name = employee_data["username"]

    # Create a CSV file with the employee ID as the filename
    filename = f"{USER_ID}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=' ')
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            csv_writer.writerow([str(USER_ID), employee_name, str(task["completed"]), task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = get_employee_data(employee_id)
    export_to_csv(employee_data, todo_data)
