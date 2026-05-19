#Take a list input from a user and print sum of odd elements in the list
lst=list(map(int,input().split()))
Sum=0
for i in lst:
    if(i%2!=0):
        Sum+=i
print(Sum)
'''
output:
2 3 4 5
8
'''
