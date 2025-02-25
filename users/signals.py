# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User

@receiver(post_save, sender=User)
def create_referral(sender, instance, created, **kwargs):
    if created:
        print(f"Referral code generated for {instance.email}: {instance.referral_code}")

