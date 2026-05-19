#To count small and capital letters
s=input()
small=0
capital=0
for i in s:
    if(ord(i)>=65 and ord(i)<=90):
        capital=capital+1
    if(ord(i)>=97 and ord(i)<=122):
        small=small+1
print(small,capital)
'''
output:
GItHUB
1 5
'''
