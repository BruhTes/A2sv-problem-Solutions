# Problem:  Network Topology - https://codeforces.com/problemset/problem/292/B

from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(int)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a] += 1
    graph[b] += 1

def isRing():
    return all(graph[i] == 2 for i in graph)

def isBus():
    ones = sum(1 for i in graph if graph[i] == 1)
    twos = sum(1 for i in graph if graph[i] == 2)
    return ones == 2 and twos == n - 2

def isStar():
    center = sum(1 for i in graph if graph[i] == n - 1)
    leaves = sum(1 for i in graph if graph[i] == 1)
    return center == 1 and leaves == n - 1

if len(graph) != n:
    print('unknown topology')
if isRing():
    print('ring topology')
elif isBus():
    print('bus topology')
elif isStar():
    print('star topology')
else:
    print('unknown topology')