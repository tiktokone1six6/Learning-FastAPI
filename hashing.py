import bcrypt

def hash_password(password:str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt=salt)

def verify_password(plain, hashed):
    return bcrypt.checkpw(plain, hashed)


my_password = b"DontH@ckM3!"
hashed = hash_password(my_password)
print(hashed)

print(verify_password(b"DontH@ckM3!", hashed))