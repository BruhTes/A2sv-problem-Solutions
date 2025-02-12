# Problem: E - From S To T - https://codeforces.com/gym/585132/problem/E


n = int(input())

for _ in range(n):
    s = input()
    t = input()
    p = input()
    
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    if i != len(s):
        print("NO")
        continue
    
    from collections import Counter

    s_count = Counter(s)
    t_count = Counter(t)
    p_count = Counter(p)
    
    possible = True
    for char in t_count:
        if p_count.get(char, 0) < t_count[char] - s_count.get(char, 0):
            possible = False
            break
    
    if possible:
        print("YES")
    else:
        print("NO")