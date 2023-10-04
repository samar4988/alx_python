import requests
import sys
import json

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

def export_todo_data_to_json(employee_id, todo_data):
    # Extract relevant information
    employee_name = employee_data.get("name")
    user_id = employee_data.get("id")

    # Create a list of tasks in the required format
    tasks_list = []
    for task in todo_data:
        task_item = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name,
        }
        tasks_list.append(task_item)

    # Create a dictionary with the user ID as the key and the tasks list as the value
    user_tasks = {f"{user_id}": tasks_list}

    # Write the JSON data to a file
    file_name = f"{user_id}.json"
    with open(file_name, "w") as json_file:
        json.dump(user_tasks, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python gather_data_from_an_API.py <employee_id>")
        sys.exit(1)