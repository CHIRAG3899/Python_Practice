#Character Pattern
#ABCD
#BCDE
#CDEF
#DEFG

n=int(input())
i=1
while i<=n:
    j=1
    str=chr(ord('A')+i-1)
    while j<=n:
        char=chr(ord(str)+j-1)
        print(char,end='')
        j+=1
    print()
    i+=1

#Print the following pattern for the given N number of rows.
#Pattern for N = 4
#A
#BC
#CDE
#DEFG
#Input format :
#Integer N (Total no. of rows)
#Output format :
#Pattern in N lines

n=int(input())
i=1
while i<=n:
    j=1
    str=chr(ord('A')+i-1)
    while j<=i:
        char=chr(ord(str)+j-1)
        print(char,end='')
        j+=1
    print()
    i+=1

#Print the following pattern for the given number of rows.
#Pattern for N = 5
#E
#DE
#CDE
#BCDE
#ABCDE
#Input format :
#N (Total no. of rows)
#Output format :
#Pattern in N lines

n=int(input())
i=1
k=n
while i<=n:
    j=1
    str=chr(ord('A')+k-1)
    while j<=i:
        char=chr(ord(str)+j-1)
        print(char,end='')
        j+=1
    print()
    i+=1
    k-=1
