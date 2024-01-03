from django.db import models
from users.models import User


# Create your models here.

class Email(models.model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipients = models.ManyToManyField(User, related_name='received_emails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_draft = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.subject} - {self.sender.email}"
