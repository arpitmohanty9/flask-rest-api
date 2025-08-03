user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"

def secure_get_admin():
    if user["access_level"] == "admin":
        return "1234"

def secure_function(func):
    if user["access_level"] == "admin":
        return func


print(secure_get_admin())
print(get_admin_password())