#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Returns number of subscribers for given subreddit else 0"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'MysubredditSubsRetreivalScript/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json()['data']['subscribers']
    return 0
