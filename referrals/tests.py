# # referrals/tests.py
# from django.contrib.auth.models import User
# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Referral

# class APITest(APITestCase):
#     def setUp(self):
#         """Create test user and authenticate"""
#         self.user = User.objects.create_user(username="testuser", password="password123")
#         self.client.post("/api/users/register/", {"username": "testuser2", "password": "password123"})
#         response = self.client.post("/api/auth/login/", {"username": "testuser", "password": "password123"})
#         self.token = response.data.get("access")
#         self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

#     def test_user_registration(self):
#         response = self.client.post("/api/users/register/", {"username": "newuser", "password": "password123"})
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_login_and_get_token(self):
#         response = self.client.post("/api/auth/login/", {"username": "testuser", "password": "password123"})
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("access", response.data)

#     def test_create_referral(self):
#         referred_user = User.objects.create_user(username="referred_user", password="password123")
#         response = self.client.post("/api/referrals/", {"referred": referred_user.id})
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_create_duplicate_referral(self):
#         referred_user = User.objects.create_user(username="referred_user", password="password123")
#         self.client.post("/api/referrals/", {"referred": referred_user.id})
#         response = self.client.post("/api/referrals/", {"referred": referred_user.id})
#         self.assertEqual(response.status_code, 400)

#     def test_get_referrals(self):
#         response = self.client.get("/api/referrals/")
#         self.assertEqual(response.status_code, 200)


from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Referral

class APITest(APITestCase):

    def setUp(self):
        """Create test user and authenticate"""
        print("\n[Setup] Creating test user and logging in...")

        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Ensure login works before proceeding
        response = self.client.post("/api/auth/login/", {"username": "testuser", "password": "password123"})
        
        if response.status_code != 200:
            print("[ERROR] Authentication failed. Check API login route.")
            print("Response:", response.content)
        else:
            print("[SUCCESS] User authenticated successfully.")
        
        self.token = response.data.get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")

    def test_user_registration(self):
        """Test user registration endpoint"""
        print("\n[TEST] Testing user registration...")

        response = self.client.post("/api/users/register/", {"username": "newuser", "password": "password123"})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "[FAIL] User registration failed!")
        print("[SUCCESS] User registered successfully.")

    def test_login_and_get_token(self):
        """Test login and token retrieval"""
        print("\n[TEST] Testing user login and token retrieval...")

        response = self.client.post("/api/auth/login/", {"username": "testuser", "password": "password123"})
        
        self.assertEqual(response.status_code, 200, "[FAIL] Login failed!")
        self.assertIn("access", response.data, "[FAIL] No access token returned!")
        
        print("[SUCCESS] Login successful. Token received.")

    def test_create_referral(self):
        """Test creating a referral"""
        print("\n[TEST] Testing referral creation...")

        referred_user = User.objects.create_user(username="referred_user", password="password123")
        response = self.client.post("/api/referrals/", {"referred": referred_user.id})
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, "[FAIL] Referral creation failed!")
        print("[SUCCESS] Referral created successfully.")

    def test_create_duplicate_referral(self):
        """Test creating a duplicate referral"""
        print("\n[TEST] Testing duplicate referral prevention...")

        referred_user = User.objects.create_user(username="referred_user", password="password123")
        self.client.post("/api/referrals/", {"referred": referred_user.id})  # First referral
        
        response = self.client.post("/api/referrals/", {"referred": referred_user.id})  # Duplicate referral
        
        self.assertEqual(response.status_code, 400, "[FAIL] Duplicate referral was allowed!")
        print("[SUCCESS] Duplicate referral correctly blocked.")

    def test_get_referrals(self):
        """Test retrieving the list of referrals"""
        print("\n[TEST] Testing referral list retrieval...")

        response = self.client.get("/api/referrals/")
        
        self.assertEqual(response.status_code, 200, "[FAIL] Failed to retrieve referrals!")
        print("[SUCCESS] Referral list retrieved successfully.")

