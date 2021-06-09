#Print the following pattern
#Pattern for N = 4
#*000*000*
#0*00*00*0
#00*0*0*00
#000***000
#Input Format :
#N (Total no. of rows)
#Output Format :
#Pattern in N lines
#Sample Input 1 :
#3
#Sample Output 1 :
#*00*00*
#0*0*0*0
#00***00

lines=int(input())
i=1  
j=1  
while i<=lines:  #this loop is used to print lines  
    j=1  
    while j<=lines:      #this loop is used to print lines  
        if i==j:  
            print("*", end='', flush=True)  
        else :  
            print("0", end='', flush=True)  
        j=j+1  
    j=j-1;  
    print("*", end='', flush=True)  
    while j>=1:  #this loop is used to print lines  
        if i==j:  
            print("*", end='', flush=True)  
        else :  
            print("0", end='', flush=True)  
        j=j-1  
    print("");  
    i=i+1  
