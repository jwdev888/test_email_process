import requests

API_KEY = "ba0908d6018cd1630aa8f7aad6670645-24bda9c7-82aeeda9"
DOMAIN = "sandbox266577ddd9264d7c828ec44cc35cf6de.mailgun.org"
RECIPIENT = "illiabublei@gmail.com"

response = requests.post(
    f"https://api.mailgun.net/v3/{DOMAIN}/messages",
    auth=("api", API_KEY),
    data={
        "from": f"Mailgun Test <mailgun@{DOMAIN}>",
        "to": RECIPIENT,
        "subject": "Hello from Mailgun",
        "text": "This is a test email from Mailgun!"
    }
)

print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Try printing the response as JSON (if it's valid)
try:
    print("Response JSON:", response.json())
except ValueError:
    print("Response is not in JSON format.")
