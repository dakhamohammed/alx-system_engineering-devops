#!/usr/bin/python3
"""function that queries the Reddit API and returns the number of
subscribers."""
import requests


def number_of_subscribers(subreddit):
	"""returns the number of subscribers (not active users, total
	subscribers), If an invalid subreddit is given return 0."""
	api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	options = {
		"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/dicor_)"
	}
	response = requests.get(api, headers=options, allow_redirects=False)
	if response.status_code == 404:
		return 0
	results = response.json().get("data")
	return results.get("subscribers")
