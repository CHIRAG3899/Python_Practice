#Print the following pattern for the given N number of rows.
#Pattern for N = 4
#4444
#333
#22
#1
#Input format :
#Integer N (Total no. of rows)
#Output format :
#Pattern in N lines

n=int(input())
while n>0:
    j=1
    
    while j<=n:
        print(n,end="")
        j+=1
    print()
    n-=1
