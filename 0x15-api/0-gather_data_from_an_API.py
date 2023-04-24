#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    # get args
    employee_id = sys.argv[1]
    # fetch url from a fake api
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(url)
    todos = response.json()

    # get the count for number of completed to-dos
    num_completed = 0
    for todo in todos:
        if todo["completed"]:
            num_completed += 1

    num_tasks = len(todos)
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    # get employee name and print the result
    employee_name = response.json()["name"]
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, num_completed, num_tasks))
    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo['title']))
