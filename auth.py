import bcrypt
import json

def load_users():
    with open("users.json") as file:
        return json.load(file)

def verify_user(username, password):
    users = load_users()
    user = users.get(username)
    
    if user:
        hashed_pw = user['password'].encode()
        if bcrypt.checkpw(password.encode(), hashed_pw):
            return user['role']
    return None
