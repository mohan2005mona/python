import re
email=input('enter valid email address')
result=re.search(r'[\w\.-]+@google.com',email)
if result:
    print("its a valid google id")
else:
    print('Your email id is invalid')
result=re.sub(r'[\w\.-]+@google.com','\2\1@gmail.com',email)
print(result)


import re
str= '808-1234 #athis is my phone number         dafdfafdafaf'
result=re.sub(r'-',' ',re.sub(r'#.*','',str))
print(result)

#program to replace the comments in the string and also the other charcters in the Phone number  i.e,. hyphen(-) and Dollar($)
import re
str= '808-12-$34 #athis is my phone number         dafdfafdafaf'
result=re.sub(r'-',' ',re.sub(r'#.*','',str))
print(result)
result=re.sub(r'\D',' ',re.sub(r'#.*','',str))
print(result)
