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

