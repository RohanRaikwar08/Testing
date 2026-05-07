class LoginException(Exception):

    def __init_(self,msg):
        super(). __init__(msg)


Login_id = "Admin"
Password = "Admin"

try:
    if Login_id == "Admn" and Password == "Admin":
        print("Valid User")


    else:
        raise LoginException("Invalid User")

except LoginException as e:
    print('LoginException', e)

