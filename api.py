from fastapi import FastAPI, Header
from schemas import Mail
from utils import send_mail
from decouple import config

app = FastAPI()

def get_credentials_by_token(auth_header: str | None):
    if not auth_header or not auth_header.startswith("Bearer "):
        return {
            "user": config("SMTP_USER"),
            "password": config("SMTP_PASSWORD")
        }

    token = auth_header.replace("Bearer ", "").strip()

    for i in range(1, 10):
        key = config(f"SMTP_TOKEN_{i}", default=None)
        if key == token:
            return {
                "user": config(f"SMTP_USER_{i}"),
                "password": config(f"SMTP_PASSWORD_{i}")
            }

    return {
        "user": config("SMTP_USER"),
        "password": config("SMTP_PASSWORD")
    }


@app.post('/send_email')
async def send_email(mail: Mail, authorization: str = Header(None)):

    creds = get_credentials_by_token(authorization)
    try:
        send_mail(
            recipient=mail.recipient,
            subject=mail.subject,
            text=mail.text,
            as_html=mail.as_html,
            smtp_user=creds['user'],
            smtp_password=creds['password']
        )
        return {'message': f'Письмо отправлено с аккаунта {creds["user"]}'}
    except Exception as e:
        return {'error': str(e)}
