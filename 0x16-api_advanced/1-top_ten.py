#!/usr/bin/python3
"""Script prints titles of top 10 hot posts for given subreddit"""
import requests


def top_ten(subreddit):
    """Method prints titles of top 10 posts given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return None
    url = "https://www.reddit.com/r/{}/hot.json?sort=top&limit=10".format(
          subreddit)
    headers = {'User-Agent': "HotpostsSubredditScript/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        """index of array of data containing subreddit info"""
        for post in response.json()['data']['children'][0:10]:
            print(post['data']['title'])
    else:
        print(None)
