import threading
import time

from .sendgrid_send_email import send_mail

#пустой список задач
TASKS = []
#количество задач к выводу
NUMBER_OF_TASKS = 10 


def add_email_to_emails(text, time):
    #добавляем в список
    TASKS.append({"text": text, "time": time})
    t = threading.Timer(time, send_mail, args=(text, ))
    t.start()

def get_last_tasks():
    return TASKS[-NUMBER_OF_TASKS:]

