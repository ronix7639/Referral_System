# referrals/models.py
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Referral(models.Model):
    referrer = models.ForeignKey(User, related_name="referrals", on_delete=models.CASCADE)
    referred = models.OneToOneField(User, related_name="referred", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.referrer.username} referred {self.referred.username}"
