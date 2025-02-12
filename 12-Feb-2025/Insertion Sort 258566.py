# Problem: Insertion Sort - https://www.hackerrank.com/challenges/insertionsort1/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    num = arr[-1]
    
    for i in range(n - 2, -1, -1):
        if num < arr[i]:
            arr[i + 1] = arr[i]
            print(" ".join(map(str, arr)))
        else:
            arr[i + 1] = num
            print(" ".join(map(str, arr)))
            break

    else:
        arr[0] = num
        print(" ".join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
