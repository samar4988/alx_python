#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the CSV format.
"""
import csv
import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
    data = api_request.text
    pjson = json.loads(data)
    data1 = api_request1.text
    pjson1 = json.loads(data1)
    
    #Export data to CSV data
    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        for item in pjson1:
            user_id = employee_id
            username = pjson['username']
            task_completed_status = item['completed']
            task_title = item['title']
            writer.writerow([user_id, username, task_completed_status, task_title])
