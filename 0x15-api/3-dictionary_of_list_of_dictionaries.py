#!/usr/bin/python3
"""
exports data in JSON format
"""
import json
from sys import argv
import requests


if __name__ == "__main__":
    """
    exports in JSON
    """

    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()

    final_dict = {}
    for user in users:
        id = user.get("id")
        all = requests.get("{}/{}/todos".format(url, id).json()

        result = []
        for task in all:
            result.append({'task': task.get('title'), 'completed': task.get
                           ('completed'), 'username': user.get('username')})
        final_dict[id] = result

    with open("todo_all_employees.json", "w") as file:
        json.dump(final_dict, file)
