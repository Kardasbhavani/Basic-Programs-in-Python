#palindrome(same as like reverse number)
n=int(input())
original=n
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(original==rev):
    print("palindrome")
else:
    print("not a palindrome")
'''
output:
1221
palindrome
'''
