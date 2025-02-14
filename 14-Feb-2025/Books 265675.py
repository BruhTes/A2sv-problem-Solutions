# Problem: Books - https://codeforces.com/contest/279/problem/B

n, m = map(int, input().split())
books = list(map(int, input().split()))

books.sort()
count = 0
i = 0
while m > 0:
    m -= books[i]
    count += 1
    i += 1

print(count - 1)