#To find count vowels & consonants
s=input()
vowel="aeiouAEIOUU"
v=0
count=0
for i in s:
    if(i in vowel):
        v=v+1
    else:
        count=count+1
print(v,count)
'''
output:
GitHUB
2 4
'''
