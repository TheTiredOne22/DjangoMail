from allauth.account.forms import SignupForm
from users.models import User
from django.utils.text import slugify
from django import forms


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = 'Email'
        self.fields['email'].widget.attrs['placeholder'] = 'john.doe'
        self.fields['email'].initial = '@domain.com'
        self.fields['full_name'] = forms.CharField(label='Full name', required=True)
        self.fields['phone_number'] = forms.CharField(label='Phone number', required=True)

    def clean_email(self):
        email = self.cleaned_data['email']

        # Ensure that the email ends with "@MySiteName.com"
        if not email.endswith("@domain.com"):
            raise forms.ValidationError("Email must end with @domain.com")

        return email

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        # Omit the line below if your CustomUser model does not have a 'domain' field
        # user.domain = "MySiteName.com"
        user.full_name = self.cleaned_data['full_name']
        user.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user
