#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If not a valid subreddit, prints None.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    # Define the Reddit API URL for getting hot posts in a subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the request to the Reddit API with allow_redirects=False
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status code indicates success
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            posts = data['data']['children']

            # Print the titles of the first 10 hot posts
            for post in posts:
                print(post['data']['title'])
        except (KeyError, IndexError):
            # If there's an issue parsing the data, print None
            print(None)
    else:
        # If the subreddit is invalid or another error occurs, print None
        print(None)

