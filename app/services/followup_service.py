from datetime import datetime, timedelta
from app.core.mailgun import send_email
from app.core.config import SIGNUP_LINK, CHATGPT_LINK
from app.services.zoho_service import check_signed_up_in_zoho

# In-memory storage for follow-up scheduling
FOLLOWUP_QUEUE = {}

def schedule_followups(email: str, project_id: str):
    """
    Schedule three follow-up emails at 1, 3, and 5 days after the initial reply.
    """
    now = datetime.utcnow()
    FOLLOWUP_QUEUE[email] = [
        {"send_at": now + timedelta(days=1), "project_id": project_id, "attempt": 1},
        {"send_at": now + timedelta(days=3), "project_id": project_id, "attempt": 2},
        {"send_at": now + timedelta(days=5), "project_id": project_id, "attempt": 3},
    ]

def run_followups():
    """
      - For each scheduled follow-up whose time has passed, check with Zoho Recruit.
      - If the expert has not signed up (dummy_value is not 'yes'), send a reminder.
      - Cancel further follow-ups if the expert is already signed up.
    """
    now = datetime.utcnow()
    to_remove = []

    for email, followups in list(FOLLOWUP_QUEUE.items()):
        updated = []
        for f in followups:
            if now >= f["send_at"]:
                # Before sending a follow-up, check if the expert has already signed up.
                if not check_signed_up_in_zoho(email):
                    body = f"""
                    <p>Hi,</p>
                    <p>Just checking in – have you signed up for Project {f['project_id']} yet?</p>
                    <p>Please sign up using the following link: <a href="{SIGNUP_LINK}?project={f['project_id']}">{SIGNUP_LINK}</a></p>
                    <p>If you have any questions, feel free to ask our ChatGPT bot: <a href="{CHATGPT_LINK}">{CHATGPT_LINK}</a></p>
                    """
                    send_email(email, f"Reminder {f['attempt']}: Complete Your Signup for Project {f['project_id']}", body)
                else:
                    # If the expert has signed up, cancel further follow-ups.
                    to_remove.append(email)
                    break
            else:
                updated.append(f)
        FOLLOWUP_QUEUE[email] = updated

    # Clean up the queue for those who have signed up.
    for email in to_remove:
        FOLLOWUP_QUEUE.pop(email, None)
