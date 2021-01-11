import re
email=input('enter valid email address')
result=re.search(r'[\w\.-]+@google.com',email)
if result:
    print("its a valid google id")
else:
    print('Your email id is invalid')
result=re.sub(r'[\w\.-]+@google.com','\2\1@gmail.com',email)
print(result)
