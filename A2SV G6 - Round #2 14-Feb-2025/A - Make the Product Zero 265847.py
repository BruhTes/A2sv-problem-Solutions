# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

N = int(input())
arr = list(map(int, input().split()))

op = 100000000

if 0 in arr:
    print(0)
else:
    for num in arr:
        op = min(op, abs(num))

    print(op)