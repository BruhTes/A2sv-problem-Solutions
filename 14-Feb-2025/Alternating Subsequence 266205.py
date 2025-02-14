# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

# def longestOnes(n, nums):

t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    maxSum = 0

    i = 0
    while i < n:
        temp = nums[i]

        if temp > 0:
            i += 1
            while i < n and nums[i] > 0:
                temp = max(temp, nums[i])
                i += 1
        else:
            i += 1
            while i < n and nums[i] < 0:
                temp = max(temp, nums[i])
                i += 1
        
        maxSum += temp
    
    print(maxSum)
        