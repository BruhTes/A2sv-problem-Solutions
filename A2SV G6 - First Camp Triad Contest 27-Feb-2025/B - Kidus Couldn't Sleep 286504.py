# Problem: B - Kidus Couldn't Sleep - https://codeforces.com/gym/589822/problem/B

n, k = map(int, input().split())
nums = list(map(int, input().split()))

windowSum = 0
for i in range(k):
    windowSum += nums[i]

totalSum = windowSum
left = 0
right = k

while right < len(nums):
    windowSum += nums[right] - nums[left]
    totalSum += windowSum
    right += 1
    left += 1

res = totalSum / (n - k + 1)
print(f"{res:.10f}")