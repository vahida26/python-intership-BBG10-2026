admin_permision={"read","write","execute"}
editor_permision={"read","write"}

user_permision=editor_permision

if admin_permision.issubset(user_permision):
    print("User has admin permissions.")
else:
    print("User does not have admin permissions.")