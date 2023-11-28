import os
from celery import Celery
from booktest import settings
import smtplib
from email.message import EmailMessage

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'booktest.settings')

app = Celery('service')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


# def mail(username, eemail):
#     email = EmailMessage()
#     email['Subject'] = 'Тест'
#     email['From'] = 'moscowciti2017@gmail.com'
#     email['To'] = f'{eemail}'
#
#     email.set_content(f'Hello {username}')
#
#     return email


@app.task()
def send_mail(username, eemail):
    mail = EmailMessage()
    mail['Subject'] = 'Тест'
    mail['From'] = 'moscowciti2017@gmail.com'
    mail['To'] = f'{eemail}'

    mail.set_content(f'Hello {username}')
    email = mail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login('moscowciti2017@gmail.com', 'agiy xnfr bdfn ysud')
        server.send_message(email)
