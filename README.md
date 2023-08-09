# News Email Sender

Welcome to the News Email Sender project! This script fetches the latest news articles related to a specific topic and sends them via email. Stay updated with the latest news right in your inbox!

## `main.py`

The `main.py` script initiates the process of fetching news articles and sending them via email. Here's how it works:

1. **News API Integration**: The script integrates with the News API to retrieve news articles based on a specified topic.

2. **Data Fetching**: It fetches the latest articles related to the given topic using the News API's endpoint. The articles are sorted by their published dates.

3. **Email Preparation**: The script prepares the email content by extracting article titles, descriptions, and URLs. It compiles this information into an email body.

4. **Email Sending**: The `send_email` function from the `send_email.py` script is used to send the compiled email to the specified recipient(s).

## `send_email.py`

The `send_email.py` script provides the functionality to send emails. It uses the `smtplib` library to send emails via SMTP. Here's how it works:

1. **Email Configuration**: The script configures the SMTP server settings, including the host, port, sender's email, and password.

2. **Email Composition**: It prepares the email message with the specified subject and body content.

3. **Email Sending**: The script establishes an SSL-secured connection to the SMTP server and sends the email to the recipient(s).

## Usage

1. Replace `topic` with the desired news topic in both `main.py` and `send_email.py`.

2. Add your email recipient(s) in the `receiver` field in the `send_email` function within `main.py`.

3. Run the `main.py` script to fetch news articles and send them via email.

## Dependencies

- Python 3.x
- `requests` library (install using `pip install requests`)

## Note

- Ensure that you have a valid API key from the News API and update the `api_key` variable in both `main.py` and `send_email.py`.

- This project is a simplified demonstration of fetching news articles and sending emails. For a production environment, consider security practices and error handling.

## Conclusion

The News Email Sender project demonstrates how Python can be used to automate fetching and delivering news articles via email. Stay informed with the latest news conveniently in your inbox!

---
