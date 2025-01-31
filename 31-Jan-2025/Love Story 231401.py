# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t = int(input())
s1 = "codeforces"

for _ in range(t):
    s2 = input()
    count = 0

    for i in range(10):
        if s1[i] != s2[i]:
            count += 1
        
    print(count)