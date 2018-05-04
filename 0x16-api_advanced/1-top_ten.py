#!/usr/bin/python3
"""
module using reddit api
"""
import requests


def top_ten(subreddit):
    """
    number of subscribers
    """
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)
    header = {'User-Agent': 'Chrome/39.2.293.01'}
    total = requests.get(url, headers=header)
    if total.status_code == 200:
        for x in total.json()['data']['children']:
            print(x['data']['title'])
    else:
        print(None)
