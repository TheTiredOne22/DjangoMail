from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from accounts.forms import CustomSignUpForm


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomSignUpForm
    model = User
    # inlines = [ProfileInline]
    list_display = (
        "email",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("full_name", "email", "password")}),
        # (
        #     "Permissions",
        #     {
        #         "fields": (
        #             "is_staff",
        #             "is_active",
        #             "is_superuser",
        #             "groups",
        #             "user_permissions",
        #         )
        #     },
        # ),
        # ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    'full_name',
                    'phone_number',
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
