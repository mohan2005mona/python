import re
list=['guru_99 get','guru99 give','guru selenium']
print(type(list))
for element in list:
    z=re.match("(g\w+)\W(g\w+)",element)
    if z:
        print(z.groups())
print(type(z))

#C:\Users\mohan.v\PycharmProjects\PythonPrograms\venv\Scripts\python.exe C:/Users/mohan.v/PycharmProjects/PythonPrograms/mohan.py
#<class 'list'>
#('guru_99', 'get')
#('guru99', 'give')
#<class 'NoneType'>

import re
list=['guru_99: sel','guru99 give','guru selenium']
string='sel'
for element in list:
    print('looking for {} in {} :'.format(string,element),end='')
    if re.search(string,element):
        print('Found')
    else:
        print('not found')
    
##C:\Users\mohan.v\PycharmProjects\PythonPrograms\venv\Scripts\python.exe C:/Users/mohan.v/PycharmProjects/PythonPrograms/mohan.py
#looking for sel in guru_99: sel :Found
#looking for sel in guru99 give :not found
#looking for sel in guru selenium :Found    

import re
list=['guru_99: sel','guru99 give','guru selenium']
string=input('what you want to find :')
for element in list:
    print('looking for {} in {} :'.format(string,element),end='')
    if re.search(string,element):
        print('Found')
    else:
        print('not found')

'''what you want to find :selenium
looking for selenium in guru_99: sel :not found
looking for selenium in guru99 give :not found
looking for selenium in guru selenium :Found
'''
import re
tar='pet:cat i love cats pet:cow i love cow'
z=re.search('\w+\Wcow',tar)
print(z.group())


import re
abc='guru9r9@google.com, carrerguru99@hotmail.com, user@gmail.com'
emails=re.findall(r'[\w\.-]+@[\w\.-]+',abc)
for email in emails:
    print(email)

#guru9r9@google.com
#carrerguru99@hotmail.com
#user@gmail.com
