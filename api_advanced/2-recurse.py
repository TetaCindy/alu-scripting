#!/usr/bin/python3
"""
Module that queries the Reddit API recursively and returns a list containing
the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Queries the Reddit API recursively and returns a list containing
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query
        hot_list (list): List to accumulate hot article titles
        after (str): Pagination token for the next page

    Returns:
        list: List of all hot article titles, or None if invalid subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:subreddit_recurse:v1.0.0'
    }
    params = {
        'limit': 100,
        'after': after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            after = data.get('data', {}).get('after', None)

            if not posts:
                return None if len(hot_list) == 0 else hot_list

            for post in posts:
                title = post.get('data', {}).get('title', '')
                hot_list.append(title)

            if after is None:
                return hot_list
            else:
                return recurse(subreddit, hot_list, after)
        else:
            return None
    except Exception:
        return None
