# referrals/serializers.py
from rest_framework import serializers
from .models import Referral
from django.contrib.auth import get_user_model

User = get_user_model()

class ReferralSerializer(serializers.ModelSerializer):
    referrer = serializers.ReadOnlyField(source="referrer.username")
    referred = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Referral
        fields = ["id", "referrer", "referred", "created_at"]
