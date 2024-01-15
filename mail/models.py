from django.db import models
from users.models import User
from cryptography.fernet import Fernet
from django.utils.crypto import get_random_string
from django.urls import reverse
import uuid

# Create your models here.

fernet_key = Fernet.generate_key()
cipher_suite = Fernet(fernet_key)


class Email(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_emails')
    recipients = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_emails')
    subject = models.CharField(max_length=255)
    body = models.TextField()
    attachments = models.FileField('Attachment', blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=16, unique=True, default=uuid.uuid4, editable=False, blank=True)
    is_draft = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    random = models.TextField()
    parent_email = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def get_absolute_url(self):
        return reverse('read', args=[str(self.slug)])

    def __str__(self):
        return f"{self.subject} - {self.sender.email}"


class Attachment(models.Model):
    file = models.FileField(upload_to='media/attachments/')
    description = models.CharField(max_length=255, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
