#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her
TODO list progress.
"""
import requests
import sys

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
    # progress report
    print("Employee {} is done with tasks {}/{}".format(
        employee_name, num_completed, num_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo['title']))
