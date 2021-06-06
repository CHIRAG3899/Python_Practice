#Nth Fibonacci Number
#Nth term of Fibonacci series F(n), where F(n) is a function, is calculated
#using the following formula -
#    F(n) = F(n-1) + F(n-2), 
#    Where, F(1) = F(2) = 1
#Provided N you have to find out the Nth Fibonacci Number.
#Input Format :
#The first line of each test case contains a real number ‘N’.
#Output Format :
#For each test case, return its equivalent Fibonacci number.
#Where ‘N’ represents the number for which we have to find its equivalent
#Fibonacci number.
#Sample Input 1:
#6
#Sample Output 1:
#8

n=int(input())
a = 1
b = 1
c=0
if n < 0:
    print("Incorrect input")
elif n == 1:
    print(a)
elif n == 2:
	print(b)
else:
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    print(c)
