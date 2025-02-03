# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())

for _ in range(n):
    string = input()
    
    if len(string) > 10:
        ls = []
        ls.append(string[0])
        ls.append(str(len(string) - 2))
        ls.append(string[-1])
        
        result = "".join(ls)
        print(result)
    else:
        print(string)