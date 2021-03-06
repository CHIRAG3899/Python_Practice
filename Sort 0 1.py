#You have been given an integer array/list(ARR) of size N that contains only
#integers, 0 and 1. Write a function to sort this array/list. Think of a
#solution which scans the array/list only once and don't require use of an
#extra array/list.
#Note:You need to change in the given array/list itself. Hence, no need to
#return or print anything. 
#Input format :
#The first line contains an Integer 't' which denotes the number of test cases
#or queries to be run. Then the test cases follow.
#First line of each test case or query contains an integer 'N' representing the
#size of the array/list.
#Second line contains 'N' single space separated integers(all 0s and 1s)
#representing the elements in the array/list.
#Output format :
#For each test case, print the sorted array/list elements in a row separated by
#a single space.
#Output for every test case will be printed in a separate line.
#Sample Input 1:
#1
#7
#0 1 1 0 1 0 1
#Sample Output 1:
#0 0 0 1 1 1 1
#Sample Input 2:
#2
#8
#1 0 1 1 0 1 0 1
#5
#0 1 0 1 0
#Sample Output 2:
#0 0 0 1 1 1 1 1
#0 0 0 1 1

from sys import stdin

def sortZeroesAndOne(arr, n) :
    left, right = 0, n-1
     
    while left < right:
        # Increment left index while we see 0 at left
        while arr[left] == 0 and left < right:
            left += 1
 
        # Decrement right index while we see 1 at right
        while arr[right] == 1 and left < right:
            right -= 1
 
        # If left is smaller than right then there is a 1 at left
        # and a 0 at right. Exchange arr[left] and arr[right]
        if left < right:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1
 
    return arr 
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) :
    for i in range(n) :
        print(arr[i], end = ' ')
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    sortZeroesAndOne(arr, n)
    printList(arr, n)
    print()

    t -= 1
