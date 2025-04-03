import requests
from app.core.config import ZOHO_API_KEY

def check_signed_up_in_zoho(email: str) -> bool:
    """
    Check if the expert is signed up in Zoho Recruit.
    """
    response = requests.get(
        f"https://zoho.yourapi.com/candidates?email={email}",
        headers={"Authorization": f"Bearer {ZOHO_API_KEY}"}
    )
    if response.status_code == 200:
        data = response.json()
        return data.get("dummy_value") == "yes"
    return False
