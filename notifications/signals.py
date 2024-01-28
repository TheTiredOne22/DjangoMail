from django.db.models.signals import post_save
from django.dispatch import receiver

from mail.models import Email, Reply
from .models import Notification


@receiver(post_save, sender=Email)
def send_email_notifications(sender, instance, created, **kwargs):
    """
    Sends email notifications to recipients when a new email is saved.
    """
    # Logic to determine the recipient and message for the notification
    if created:
        recipient = instance.recipient
        sender_name = instance.sender
        subject = instance.subject
        body = instance.body

        notification = Notification.objects.create(user=recipient,
                                                   notification_type=Notification.NotificationType.EMAIL,
                                                   sender_name=sender_name, subject=subject, body=body,
                                                   related_email=instance,
                                                   message=f"New Message from {sender_name}: {subject} - {body}")
        notification.generate_url()


@receiver(post_save, sender=Reply)
def send_reply_notification(sender, instance, created, **kwargs):
    # Logic to determine the recipient and message for the notification
    email_instance = instance.email
    recipient = instance.get_notification_recipient()
    sender_name = instance.sender
    body = instance.body

    if recipient:
        notification = Notification.objects.create(user=recipient,
                                                   notification_type=Notification.NotificationType.REPLY,
                                                   sender_name=sender_name, body=body, related_email=email_instance,
                                                   message=f"Reply from {sender_name}: - {body}")
        notification.generate_url()
