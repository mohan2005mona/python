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

# Program to replace the string pattern with other pattern - here we are using multiple combination of pattern to search and replace with the string
import re
str= '''U.S. stock-index futures pointed 
to a solidly higher open on Monday,
indicating that major
benchmarks were poised to USA reboundfrom last week's sharp decline,
\nwhich represented their biggest weekly drops in months.'''
i=re.sub(r'USA|U.S.|US','United States',str)
print(i)
