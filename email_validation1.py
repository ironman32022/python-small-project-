import re
email_condition="^[a-z]+[\.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('enter your email :')
if re.search(email_condition,user_email):
    print("Right Email")
else:
    print("Wrong Email")    