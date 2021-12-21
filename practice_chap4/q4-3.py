s="Python is widely used by a number of big companies"
word="aeiou"
print("모음 : ",end="")
count = 0
n=0
while n < len(s):
    if s[n] in word :
        count=count+1
        print(s[n],end=" ")
    n = n+1
print()
print("모음 개수 : %s" %count)