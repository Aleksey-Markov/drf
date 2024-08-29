
from celery import shared_task


@shared_task
def send_email(subject, body, recipient_list):
    pass


@shared_task
def sending():
    print("ZHOPA")
