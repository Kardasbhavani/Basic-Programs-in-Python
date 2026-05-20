#To reverse the elements in the list
lst=list(map(int,input().split()))
n=len(lst)
for i in range(n//2):
    lst[i],lst[n-i-1]=lst[n-i-1],lst[i]
print(lst)
'''
output:
1 2 3 4 5 6
[6, 5, 4, 3, 2, 1]
'''
