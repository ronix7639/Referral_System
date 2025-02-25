# referrals/urls.py
# referrals/urls.py
from django.urls import path
from .views import ReferralListCreateView

urlpatterns = [
    path("", ReferralListCreateView.as_view(), name="referrals-list-create"),
]
