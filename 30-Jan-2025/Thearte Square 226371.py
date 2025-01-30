# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

import sys
n = list(map(int, input().split(" ")))

x, y = 0, 0
if n[0] % n[2] == 0:
    x = n[0] // n[2]
else:
    x = n[0] // n[2] + 1

if n[1] % n[2] == 0:
    y = n[1] // n[2]
else:
    y = n[1] // n[2] + 1

print(x * y)
