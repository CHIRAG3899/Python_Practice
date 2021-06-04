#Write a program that performs the tasks of a simple calculator. The program should first take an integer as input and then based on that integer perform the task as given below.
#1. If the input is 1, then 2 integers are taken from the user and their sum is printed.
#2. If the input is 2, then 2 integers are taken from the user and their difference(1st number - 2nd number) is printed.
#3. If the input is 3, then 2 integers are taken from the user and their product is printed.
#4. If the input is 4, then 2 integers are taken from the user and the quotient obtained (on dividing 1st number by 2nd number) is printed.
#5. If the input is 5, then 2 integers are taken from the user and their remainder(1st number mod 2nd number) is printed.
#6. If the input is 6, then the program exits.
#7. For any other input, then print "Invalid Operation".
#Note: Each answer in next line.
#Input format:
#Take integers as input, in accordance to the description of the question. 
#Output format:
#The output lines must be as prescribed in the description of the question.
#Sample Input:
#3
#1
#2
##4
#4
#2
#1
#3
#2
#7
#6
#Sample Output:
#2
#2
#5
#Invalid Operation

o=int(input())
while(o!=6):
    if(o<=5 and o>=1):
        a=int(input())
        b=int(input())
    if (o==1):
        print(a+b)
    if(o==2):
        print(a-b)
    if(o==3):
        print(a*b)
    if(o==4):
        print(a//b)
    if(o==5):
        print(a%b)
    elif(o<1 or o>6):
        print('Invalid Operation')
    o=int(input())
