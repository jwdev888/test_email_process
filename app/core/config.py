import os
from dotenv import load_dotenv

load_dotenv()

# Mailgun API configuration
MAILGUN_API_KEY = os.getenv("MAILGUN_API_KEY")
MAILGUN_DOMAIN = os.getenv("MAILGUN_DOMAIN")
FROM_EMAIL = os.getenv("FROM_EMAIL", "make@com")

# Zoho Recruit API configuration
ZOHO_API_KEY = os.getenv("ZOHO_API_KEY")

# External links and document locations
SIGNUP_LINK = "https://make.com/signup"
CHATGPT_LINK = "https://chat.openai.com/g/model"
KNOWLEDGE_DOC_LINK = "https://make.com/docs/project_guide.pdf"
