from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from .managers import UserManager


# Create your models here.


class User(AbstractUser):
    """
    Default custom user model for My Awesome Project.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    full_name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
