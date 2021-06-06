#Print the following pattern for the given N number of rows.
#Pattern for N = 4
#1
#11
#202
#3003
#Input format :
#Integer N (Total no. of rows)
#Output format :
#Pattern in N lines

num=int(input())
for i in range(1,num+1):
    for j in range(0,i):
        x=i-1
        if x==0:
            print(1,end="")
        else:
            if x==j or j==0:
                print(x,end="")
            else:print(0,end="")
    print("")

#Print the following pattern for the given N number of rows.
#Pattern for N = 4
#1234
#123
#12
#1
#Input format :
#Integer N (Total no. of rows)
#Output format :
#Pattern in N lines

n=int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end='')
    print()
