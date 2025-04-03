from fastapi import FastAPI
from app.routers import email_router
from app.services.followup_service import run_followups

app = FastAPI()

# Include the email reply endpoint
app.include_router(email_router.router)

@app.get("/run-followups")
def run():
    """
    Endpoint to manually trigger follow-up processing.
    In a production environment, this could be scheduled with a task scheduler.
    """
    run_followups()
    return {"status": "Follow-ups processed."}
