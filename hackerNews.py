"""
Script for Hacker News
"""

import requests

# Base API URL
BASE_URL = "https://hacker-news.firebaseio.com/v0"

# Get top story IDs
response = requests.get(f"{BASE_URL}/topstories.json")
if response.status_code == 200:
    top_story_ids = response.json()[:5]  # Get top 5 story IDs
else:
    print("Failed to fetch top stories")
    top_story_ids = []

# Fetch details for each top story
for story_id in top_story_ids:
    story_url = f"{BASE_URL}/item/{story_id}.json"
    story_response = requests.get(story_url)

    if story_response.status_code == 200:
        story = story_response.json()
        print(f"Title: {story.get('title')}")
        print(f"URL: {story.get('url', 'No URL available')}")
        print(f"Score: {story.get('score')}")
        print(f"By: {story.get('by')}\n")
    else:
        print(f"Failed to fetch story {story_id}")