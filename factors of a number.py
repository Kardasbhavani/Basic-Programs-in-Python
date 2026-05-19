# To find factors of a number
n=int(input())
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        print(i)
        if(i!=n//i):
            print(n//i)
'''
output :
36
1
36
2
18
3
12
4
9
6
'''
