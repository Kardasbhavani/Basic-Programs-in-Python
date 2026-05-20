#To convert list to dictionary
lst=list(map(int,input().split()))
d={}
for i in lst:
    if(i in d):
        d[i]=d[i]+1
    else:
        d[i]=1
print(d)
'''
output:
1 1 2 1 3 3
{1: 3, 2: 1, 3: 2}
'''
