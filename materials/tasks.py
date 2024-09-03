
from celery import shared_task
from materials.models import Subscription
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER


@shared_task
def send_email(course):
    updates = Subscription.objects.filter(course=course.id)
    for update in updates:
        send_mail(
            subject="Курс обновлен!",
            message=f"Курс {course.title} был изменен.",
            from_email=EMAIL_HOST_USER,
            recipient_list=[update.user.email],
        )

