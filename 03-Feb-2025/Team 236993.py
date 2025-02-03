# Problem: Team - https://codeforces.com/contest/231/problem/A

import sys
import math
import itertools
from collections import defaultdict, Counter, deque
from functools import lru_cache
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush

input = sys.stdin.readline

def ints():
    return map(int, input().split())

def solve(arr):
    count_z = 0
    count_o = 0

    for num in arr:
        if num == 0:
            count_z += 1
        else:
            count_o += 1
    
    if count_o > count_z:
        return 1
    else:
        return 0

def main():
    t = int(input().strip()) 
    
    count = 0

    for _ in range(t):
        arr = list(ints())
        count += solve(arr)
    
    print(count)

if __name__ == "__main__":
    main()
