#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""
import requests
import sys
import csv
if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    num_completed = 0
    for todo in todos:
        if todo["completed"]:
            num_completed += 1

    num_tasks = len(todos)
    # Get the name of the employee
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_name = response.json()["name"]
    csv_data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    for todo in todos:
        csv_data.append(
            [employee_id, employee_name, todo['completed'], todo['title']])
    file_name = f"{employee_id}.csv"

    with open(file_name, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)
