#!/usr/bin/python3
"""
module using reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    header = {'User-Agent': 'Chrome/39.2.293.01'}
    total = requests.get(url, headers=header)
    if total.status_code == 200:
        return total.json()['data']['subscribers']
    else:
        return 0
