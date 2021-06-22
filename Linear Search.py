n=int(input())
el=int(input())
isFound=False
li=[int(x) for x in input().split()]
for i in range(0,n):
    if li[i]==el:
        print(i)
        isFound=True
        break
if isFound is False:
    print(-1)
        
