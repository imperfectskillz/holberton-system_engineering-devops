#!/usr/bin/python3
"""
retrieve data using API
"""
from sys import argv
import requests


if __name__ == "__main__":
    """
    displays todo task
    """

    url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    user = requests.get(url).json()
    user_name = user.get("name")

    tod = "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    all = requests.get(tod).json()

    count = 0
    for task in all:
        if task.get("completed") is True:
            count += 1

    print("Employee {} is done with tasks({}/{}):".format(user_name, count,
                                                          len(all)))
    for task in all:
        if task.get("completed") is True:
            print("\t {}".format(task.get("title")))
