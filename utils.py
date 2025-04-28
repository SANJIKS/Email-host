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

def send_mail(recipient, subject, text, as_html=False):
    try:
        smtp_server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(SMTP_USER, SMTP_PASSWORD)

        msg = MIMEMultipart()
        msg['From'] = SMTP_USER
        msg['To'] = recipient
        msg['Subject'] = subject
        if as_html:
            msg.attach(MIMEText(text, 'html'))
        else:
            msg.attach(MIMEText(text, 'plain'))

        smtp_server.sendmail(SMTP_USER, recipient, msg.as_string())

    except Exception as e:
        print(f"Ошибка при отправке письма: {e}")

    finally:
        smtp_server.quit()


if __name__ == '__main__':
    send_mail('sanzarmaratov588@gmail.com', 'hahaa', 'sigma mail smtp sent')