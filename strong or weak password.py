#To check whether the password is strong or weak
s=input()
small=0    #[a to z]-[97 to 122]
capital=0  #[A to Z]-[65 to 90]
numbers=0  #[0 to 9]-[48 to 57]
special=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        capital=capital+1
    elif(ord(i)>=97 and ord(i)<=122):
        small=small+1
    elif(ord(i)>=48 and ord(i)<=57):
        numbers=numbers+1
    else:
        special=special+1
if(len(s)==0):
    print("Please enter a password")
else:
    if(len(s)>=8 and capital>0 and small>0 and special>0 and numbers>0):
        print("Strong Password")
    else:
        print("Weak password")
'''
output:
shiVa12/1/2007
Strong Password
'''
