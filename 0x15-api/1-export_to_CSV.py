#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress."""
import csv
import requests
import sys


if __name__ == "__main__":
    # get args
    employee_id = sys.argv[1]
    # retrieve url
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # get the number of completed to-dos
    num_completed = 0
    for todo in todos:
        if todo["completed"]:
            num_completed += 1

    # retrieve the todo and save as csv
    num_tasks = len(todos)
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_name = response.json()["name"]
    csv_data = []
    for todo in todos:
        csv_data.append(
            [employee_id, employee_name, todo['completed'], todo['title']])
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(csv_data)
