#!/usr/bin/python3
"""
Script to test the top_ten function from the 1-top_ten module.
"""

import sys

if __name__ == '__main__':
    # Import the top_ten function from the 1-top_ten module
    top_ten = __import__('1-top_ten').top_ten

    # Check if a subreddit argument is provided
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Call the top_ten function with the provided subreddit
        top_ten(sys.argv[1])
