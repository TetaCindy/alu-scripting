#!/usr/bin/python3
"""
Module that queries the Reddit API recursively, parses titles of all hot
articles, and prints a sorted count of given keywords.
"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Queries the Reddit API recursively and prints a sorted count of
    given keywords from all hot article titles.

    Args:
        subreddit (str): The name of the subreddit to query
        word_list (list): List of keywords to count (case-insensitive)
        after (str): Pagination token for the next page
        word_count (dict): Dictionary to accumulate word counts

    Returns:
        None: Prints sorted word counts
    """
    if word_count is None:
        word_count = {}

    if subreddit is None or not isinstance(subreddit, str):
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'python:subreddit_word_count:v1.0.0'
    }
    params = {
        'limit': 100,
        'after': after
    }

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])
        after = data.get('data', {}).get('after', None)

        if not posts and after is None:
            return

        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            words = title.split()

            for word in words:
                for keyword in word_list:
                    if word == keyword.lower():
                        key = keyword.lower()
                        word_count[key] = word_count.get(key, 0) + 1

        if after is None:
            if word_count:
                sorted_words = sorted(word_count.items(),
                                      key=lambda x: (-x[1], x[0]))
                for word, count in sorted_words:
                    print("{}: {}".format(word, count))
        else:
            count_words(subreddit, word_list, after, word_count)

    except Exception:
        return
