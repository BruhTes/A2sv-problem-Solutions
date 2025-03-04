# Problem: Red and Blue - https://codeforces.com/contest/1469/problem/B

t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    l = list(map(int, input().split()))

    max1 = r[0]
    prefix1 = max1
    for i in range(1, n):
        prefix1 += r[i]
        max1 = max(max1, prefix1)
    max2 = l[0]
    prefix2 = max2
    for i in range(1, m):
        prefix2 += l[i]
        max2 = max(max2, prefix2)

    print((max1 if max1 >= 0 else 0) + (max2 if max2 >= 0 else 0))