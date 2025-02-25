# users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    referral_code = models.CharField(max_length=10, unique=True, blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Change related name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Change related name
        blank=True
    )
