#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress
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

def export_todo_data(todo_data):
    employee_todo_dict = {}
    for task in todo_data:
        user_id = task["userId"]
        if user_id not in employee_todo_dict:
            employee_todo_dict[user_id] = []
        
        employee_todo_dict[user_id].append({
            "username": task["title"],
            "task": task["title"],
            "completed": task["completed"]
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employee_todo_dict, json_file, indent=4)

def display_todo_progress(employee_data, todo_data):
    # Extract relevant information
    employee_name = employee_data.get("name")
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_data, todo_data = get_employee_data(employee_id)
    display_todo_progress(employee_data, todo_data)
    export_todo_data(todo_data)
