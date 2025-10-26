# API Advanced

## Description
Python scripts that interact with the Reddit API to retrieve subreddit information.

## Requirements
* Ubuntu 14.04 LTS
* Python 3.4.3
* PEP 8 style
* Requests module

## Tasks

### 0. How many subs?
Function that queries the Reddit API and returns the number of subscribers for a given subreddit.

**File:** `0-subs.py`

**Prototype:** `def number_of_subscribers(subreddit)`

**Returns:** Number of subscribers, or 0 if invalid subreddit

**Usage:**
```bash
python3 0-main.py programming
```

### 1. Top Ten
Function that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

**File:** `1-top_ten.py`

**Prototype:** `def top_ten(subreddit)`

**Prints:** Titles of top 10 hot posts, or None if invalid subreddit

**Usage:**
```bash
python3 1-main.py programming
```

### 2. Recurse it!
Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.

**File:** `2-recurse.py`

**Prototype:** `def recurse(subreddit, hot_list=[])`

**Returns:** List of all hot article titles, or None if invalid subreddit

**Features:**
* Uses recursion (no loops for pagination)
* Handles Reddit API pagination with `after` parameter
* Gets all hot articles from all pages

**Usage:**
```bash
python3 2-main.py programming
```

### 3. Count it!
Recursive function that queries the Reddit API, parses titles of all hot articles, and prints a sorted count of given keywords.

**File:** `3-count.py`

**Prototype:** `def count_words(subreddit, word_list)`

**Prints:** Sorted count of keywords (descending by count, then alphabetically)

**Features:**
* Case-insensitive keyword matching
* Exact word matching (no partial matches)
* Counts all occurrences across all titles
* Handles duplicate keywords in word_list
* Prints nothing for invalid subreddits or no matches

**Usage:**
```bash
python3 3-main.py programming 'python java javascript'
python3 3-main.py programming 'JavA java'
```

## Repository
* **GitHub repository:** `alu-scripting`
* **Directory:** `api_advanced`
