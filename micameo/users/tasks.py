from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage

from config import celery_app

User = get_user_model()


@celery_app.task()
def get_users_count():
    """A pointless Celery task to demonstrate usage."""
    return User.objects.count()


@celery_app.task()
def send_email(message, to_email):
    mail_subject = 'Activate your micameo account.'
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()

    return None


@celery_app.task()
def send_email_notification(subject, message, to_email):
    email = EmailMessage(subject, message, to=to_email)
    email.send()

    return None
