from pydantic import BaseModel

class EmailReply(BaseModel):
    expert_email: str
    project_id: str
