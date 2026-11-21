class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age<0 or age>120:
        raise InvalidAgeError("invalid age!")
    print("registration successful")
register_user(25)