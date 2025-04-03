import requests
from app.core.config import MAILGUN_API_KEY, MAILGUN_DOMAIN, FROM_EMAIL

def send_email(to_email: str, subject: str, body: str):
    """
    Send an email using Mailgun api.
    """
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": FROM_EMAIL,
            "to": to_email,
            "subject": subject,
            "html": body
        }
    )
