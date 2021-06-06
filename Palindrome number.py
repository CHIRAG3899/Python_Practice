#Palindrome number
#Write a program to determine if given number is palindrome or not.
#Print true if it is palindrome, false otherwise.
#Palindrome are the numbers for which reverse is exactly same as the
#original one.
#Sample Input 1 :
#121
#Sample Output 1 :
#true
#Sample Input 2 :
#1032
#Sample Output 2 :
#false

num=int(input())
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("true")
else:
    print("false")
