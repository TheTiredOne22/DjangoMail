from .models import Email
from django.forms import ModelForm


class EmailComposeForm(ModelForm):
    class Meta:
        model = Email
        fields = ['recipients', 'subject', 'body']


class EmailReplyForm(ModelForm):
    class Meta:
        model = Email
        fields = ['body']
