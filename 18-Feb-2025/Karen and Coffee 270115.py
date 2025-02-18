# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

n, k, q = map(int, input().split())
max_temp = 200000

freq = [0 for i in range(max_temp + 1)]

for _ in range(n):
    start, end = map(int, input().split())
    freq[start] += 1
    if end + 1 < len(freq):
        freq[end + 1] -= 1

for i in range(1, len(freq)):
    freq[i] = freq[i - 1] + freq[i]

# prepare the admissible prefix Sum
admissible = [0 for i in range(max_temp + 1)]
for i in range(1, len(admissible)):
    admissible[i] = admissible[i - 1] + (1 if freq[i] >= k else 0)

# process the queries
for _ in range(q):
    start, end = map(int, input().split())
    print(admissible[end] - admissible[start - 1])