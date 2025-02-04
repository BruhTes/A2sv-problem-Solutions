# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E


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





    # sp = s + p
    # dic = {}
    # # dic2 = {}
    

    # for char in sp:
    #     dic[char] = dic.get(char, 0) + 1

    # t_non = ""
    # for char in t:
    #     if char not in t_non:
    #         t_non += char
    
    # count = 0
    # for char in t_non:
    #     if char in dic:
    #         count += dic[char]
    

    # if count >= len(t) and (s[0] == t[0] or s[-1] == t[-1]):
    #     print("YES")
    # else:
    #     print("NO")

    # # sp = ""
    # # dic = {}
    