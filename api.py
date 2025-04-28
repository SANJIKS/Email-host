from fastapi import FastAPI
from schemas import Mail
from utils import send_mail

app = FastAPI()

@app.post('/send_email')
async def send_email(mail: Mail):
    try:
        print(send_mail(mail.recipient, mail.subject, mail.text, mail.as_html))
        return {'message': 'mail sent!'}
    except Exception as e:
        return {'error': e}