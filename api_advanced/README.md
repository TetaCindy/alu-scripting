PI Advanced

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

## Repository
* **GitHub repository:** `alu-scripting`
* **Directory:** `api_advanced`
