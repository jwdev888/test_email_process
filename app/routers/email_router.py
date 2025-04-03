from fastapi import APIRouter, BackgroundTasks
from app.models.schemas import EmailReply
from app.services.followup_service import schedule_followups
from app.core.mailgun import send_email
from app.core.config import SIGNUP_LINK, CHATGPT_LINK, KNOWLEDGE_DOC_LINK

router = APIRouter()

@router.post("/email-reply")
async def handle_reply(reply: EmailReply, background_tasks: BackgroundTasks):
    """
      first, Send an immediate auto-reply with a signup link, ChatGPT link, and a knowledge document.
      next, Schedule follow-up emails if the expert does not complete the signup.
    """
    body = f"""
    <p>Hi,</p>
    <p>Thank you for your interest in Project {reply.project_id}!</p>
    <p>Please sign up using this link: <a href="{SIGNUP_LINK}?project={reply.project_id}">{SIGNUP_LINK}</a></p>
    <p>You can ask any questions using our ChatGPT bot: <a href="{CHATGPT_LINK}">{CHATGPT_LINK}</a></p>
    <p>Also, please review our knowledge document for more details: <a href="{KNOWLEDGE_DOC_LINK}">Knowledge Base</a></p>
    """
    send_email(reply.expert_email, f"Project {reply.project_id} – Next Steps", body)
    
    # Schedule follow-up emails to remind the expert to complete the signup if they haven't already.
    background_tasks.add_task(schedule_followups, reply.expert_email, reply.project_id)
    
    return {"status": "Initial auto-reply sent and follow-ups scheduled."}
