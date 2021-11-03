# Using the GitHub API, can you find the most popular Python repositories in GitHub (use "stars" as a metric)

import requests
response = requests.get('https://api.github.com/search/repositories?q=language:python&sort=stars')
data = response.json()
print(data)

# Find the GitHub users with the most followers
response = requests.get('https://api.github.com/search/users?q=followers:>=1000&sort=followers&order=desc')
data = response.json()
print(data)

#Find a list of Python repositories with the most open "help wanted" issues
response = requests.get('https://api.github.com/search/users?q=help:>=1000&sort=followers&order=desc')
data = response.json()
print(data)
