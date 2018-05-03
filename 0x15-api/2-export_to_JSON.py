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

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = requests.get(url).json()
    user_name = user.get("name")

    tod = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    all = requests.get(tod).json()

    result = []
    for task in all:
        result.append({'task': task.get('title'), 'completed': task.get
                       ('completed'), 'username': user_name})

    result_dict = {}
    result_dict[argv[1]] = result

    with open("{}.json".format(argv[1]), "w") as file:
        json.dump(result_dict, file)
