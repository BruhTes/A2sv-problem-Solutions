# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

n = int(input())
nums = list(map(int, input().split()))

nums.sort()
if len(nums) % 2 == 0:
    print(nums[(len(nums) // 2) - 1])
else:
    print(nums[(len(nums) // 2)])