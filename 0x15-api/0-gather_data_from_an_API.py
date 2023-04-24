#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(url)
    todos = response.json()

    num_completed = 0
    for todo in todos:
        if todo["completed"]:
            num_completed += 1

    num_tasks = len(todos)
    url = f"https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_name = response.json()["name"]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed, num_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo['title']))
