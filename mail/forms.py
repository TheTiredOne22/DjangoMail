from django import forms
from django.core.exceptions import ValidationError

from users.models import User
from .models import Email, Reply


class EmailComposeForm(forms.ModelForm):
    recipient = forms.EmailField()

    class Meta:
        model = Email
        fields = ['recipient', 'subject', 'body']

    def clean_recipient(self):
        email = self.cleaned_data.get('recipient')
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            raise ValidationError("User with this email does not exist.")
        return user


class EmailReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
