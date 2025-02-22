# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import *
import math
 
def solve():
    n = int(input(''))
 
    arr = list(map(int, input().split()))
 
    ans = float("inf")
    count = Counter(arr)
    occ = Counter(list(count.values()))

    ans = float("inf")
    for i in occ.keys():
        cur = 0
        for j in occ.keys():
            if i > j:
                cur += j * occ[j] 
            elif i < j:
                cur += (j - i) * occ[j]
        ans = min(ans, cur)
 
 
    print(ans)
 
if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()