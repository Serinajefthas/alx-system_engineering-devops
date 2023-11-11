#!/usr/bin/python3
"""Script prints titles of top 10 hot posts for given subreddit
using recursive function"""
import requests


def recurse(subreddit, hot_list=[]):
    """Recursively retrieve titles of hot posts of subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': "HotpostsSubredditRecursive/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        for post in response.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if response.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
