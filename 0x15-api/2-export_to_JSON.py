#!/usr/bin/python3
"""Extend your Python script to export data in the JSON format.
Requirements:
    Records all tasks that are owned by this employee
    File name must be: USER_ID.json."""
import json
import requests
import sys


if __name__ == "__main__":
    # get args
    user_id = sys.argv[1]
    # fetch url from a fake api
    url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)
    response = requests.get(url)
    todos = response.json()

    # retrieve username and save as csv
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user_name = response.json()["username"]
    list_json = []
    keys = ["task", "completed", "username"]
    for todo in todos:
        values = [todo.get("title"), todo.get("completed"), user_name]
        dict1 = dict(zip(keys, values))
        list_json.append(dict1)
    dict = dict({str(user_id): list_json})
    file_name = "{}.json".format(user_id)
    with open(file_name, "w") as jsonfile:
        json.dump(dict, jsonfile)
