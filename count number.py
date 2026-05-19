#To count number of individual terms
n=int(input())
count=0
while(n>0):
    n=n//10
    count=count+1
print(count)
'''
output:
1001
4
'''
