from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy


def custom_logout_view(request):
    # Call logout method to immediately log out the user
    logout(request)
    # Redirect to the login page after logout
    return redirect(reverse_lazy('account_login'))
