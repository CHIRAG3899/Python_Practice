#Print the following pattern for the given N number of rows.
#Pattern for N = 4
#1
#11
#121
#1221
#Input format :
#Integer N (Total no. of rows)
#Output format :
#Pattern in N lines

n=int(input())
i=1
while i<=n:
    for j in range(1, i + 1, 1):
        if (j == 1 or j == i):
            print(1, end = "")
        else:
            print(2, end = "")
    i+=1
    print('\n', end = "")
