# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585132/problem/C

t = int(input())

for _ in range(t):
    a, b = input().split()
    
    # if len(a) > len(b):
    if ("L" in a and "L" in b)  or ("S" in a and "S" in b) or ("M" in a and "M" in b):
        if len(a) == len(b):
            print("=")
        elif len(a) > len(b):
            if "S" in a:
                print("<")
            else:
                print(">")
        else:
            if "S" in a:
                print(">")
            else:
                print("<")
    else:
        if ("L" in a and "S" in b) or ("L" in a and "M" in b):
            print(">")
        elif ("S" in a and "L" in b) or ("M" in a and "L" in b):
            print("<")
        elif ("S" in a and "M" in b):
            print("<")
        elif ("M" in a and "S" in b):
            print(">")
                