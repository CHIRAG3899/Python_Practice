#An array is a type of data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .
#Reverse an array of integers.
#Complete the function reverseArray in the editor below.


import math
import os
import random
import re
import sys


def reverseArray(a):
    temp = []
    size = len(a)
    for i in range(size-1, -1, -1):
        temp.append(a[i])
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
