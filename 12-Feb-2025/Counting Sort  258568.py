# Problem: Counting Sort  - https://www.hackerrank.com/challenges/countingsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def countingSort(arr):
    counter = [0 for i in range(100)]
    
    for num in arr:
        counter[num] += 1
    
    return counter
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
