import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from decouple import config

SMTP_HOST = config('SMTP_HOST')
SMTP_PORT = config('SMTP_PORT')
SMTP_USER = config('SMTP_USER')
SMTP_PASSWORD = config('SMTP_PASSWORD')

smtp_server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
smtp_server.starttls()
smtp_server.login(SMTP_USER, SMTP_PASSWORD)

def send_mail(recipient, subject, text, as_html=False, smtp_user=None, smtp_password=None):
    try:
        smtp_server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(smtp_user, smtp_password)

        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'html' if as_html else 'plain', _charset='utf-8'))

        smtp_server.sendmail(smtp_user, recipient, msg.as_string())
    finally:
        smtp_server.quit()


if __name__ == '__main__':
    send_mail(SMTP_USER, 'Hahahahahahahahahh', 'sigma mail smtp sent')