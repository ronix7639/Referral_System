# users/utils.py
import bcrypt as bc

def hash_password(password):
    return bc.hashpw(password.encode(), bc.gensalt()).decode()

def check_password(password, hashed):
    return bc.checkpw(password.encode(), hashed.encode())