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
    # fetch url from a fake api
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)
    response = requests.get(url)
    todos = response.json()

    # get the count for number of completed to-dos
    num_completed = 0
    for todo in todos:
        if todo["completed"]:
            num_completed += 1

    num_tasks = len(todos)
    # retrieve employee name and save as csv
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_name = response.json()["name"]
    csv_data = []
    for todo in todos:
        csv_data.append(
            [employee_id, employee_name, todo['completed'], todo['title']])
    file_name = "{}.csv".format(employee_id)

    with open(file_name, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(csv_data)
