import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(text):
   message = Mail(
       from_email='basvad@outlook.com',
       to_emails='basvadium@yandex.ru',
       subject='Sending with Twilio SendGrid is Fun',
       html_content='<strong></strong>'.format(text))
   try:
       #sg = SendGridAPIClient(SENDGRID_API_KEY)
       sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
       print(sg)
       response = sg.send(message)
       print(response.status_code)
       print(response.body)
       print(response.headers)
   except Exception as e:
       #print(e.message)
       print('Ошибка')