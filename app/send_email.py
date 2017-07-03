import requests
from app.config import api_key

def send_email(msg):
    response = requests.post(
        "https://api.mailgun.net/v3/reformmidems.com/messages",
        auth=("api", api_key),
        data = {
            "from": "Ryan Wiley <mailgun@reformmidems.com>",
            "to": msg.send_to,
            "subject": msg.subject,
            "text": msg.body
        }
    )
