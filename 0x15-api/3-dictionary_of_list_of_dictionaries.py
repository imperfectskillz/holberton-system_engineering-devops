#!/usr/bin/python3
"""
retrieve data using API export in CSV
"""
import json
from sys import argv
import requests


if __name__ == "__main__":
    """
    exports CSV
    """

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    final_dict = {}
    for user in users:
        id = user.get("id")
        all = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(id).json()

        result = []
        for task in all:
            task_dict = {}
            task_dict.append({'task': task.get('title'), 'completed': task.get
                       ('completed'), 'username': user.get("username")})
            result.append(task_dict)
        final_dict[id] = result

    with open("todo_all_employees.json", "w") as file:
        json.dump(final_dict, file)
