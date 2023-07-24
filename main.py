# This program does not have a GUI
from send_email import send_email
import requests

topic = "tesla"
api_key = "de4b7cde6e684f208f9d6599deff6d3f"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
        "from=2023-06-24&" \
        "sortBy=publishedAt&" \
        "apiKey=de4b7cde6e684f208f9d6599deff6d3f&"\
        "language=en"

# Make request
request = requests.get(url)

# Set a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:

    if article["title"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
