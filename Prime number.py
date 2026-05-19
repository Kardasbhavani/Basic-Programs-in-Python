#To check whether the given number is prime or not
n=int(input())
count=0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        count=count+1
        if(i!=n//i):
            count=count+1
if(count==2):
    print("prime number")
else:
    print("not a prime number")
'''
output:
10
not a prime number
'''
