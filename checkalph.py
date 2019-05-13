import re
n=input()
if (re.findall('[a-zA-Z]',n) )and( re.findall('[0-9]',n)):
    print("Yes")
else: 
    print("No")
