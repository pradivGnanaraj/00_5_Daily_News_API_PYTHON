# This program does not have a GUI

import requests

api_key = "de4b7cde6e684f208f9d6599deff6d3f"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-24&sortBy=publishedAt&apiKey=de4b7cde6e684f208f9d6599deff6d3f"

request = requests.get(url)
content = request.text
print(content)
