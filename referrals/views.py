# referrals/views.py
from rest_framework import generics, permissions
from .models import Referral
from .serializers import ReferralSerializer
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class ReferralListCreateView(generics.ListCreateAPIView):
    serializer_class = ReferralSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return only the referrals where the user is the referrer."""
        return Referral.objects.filter(referrer=self.request.user)

    def perform_create(self, serializer):
        """Ensure the referrer is always the authenticated user."""
        referred_user = serializer.validated_data["referred"]
        if Referral.objects.filter(referred=referred_user).exists():
            raise ValidationError("This user has already been referred.")
        serializer.save(referrer=self.request.user)
