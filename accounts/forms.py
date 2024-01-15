from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

from users.models import User
from django.utils.text import slugify
from django import forms
from django.conf import settings
import re


class CustomSignUpForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)
        
        self.fields['full_name'] = forms.CharField(label='Full Name', required=True)
        self.fields['phone_number'] = forms.CharField(max_length=20)

    def save(self, request):
        user = super(CustomSignUpForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
