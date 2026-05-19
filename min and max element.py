#To find minimum and maximum number in list
n=list(map(int,input().split()))
small=n[0]
large=n[0]
for i in n:
    if i<small:
        small=i
    if i>large:
        large=i
print("Min:",small)
print("Max:",large)
'''
output:
5 2 7 3 9 1
Min: 1
Max: 9
'''
