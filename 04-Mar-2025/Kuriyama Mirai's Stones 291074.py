# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

n = int(input())
nums = list(map(int, input().split()))
nums2 = sorted(nums)

for i in range(1, n):
    nums[i] = nums[i] + nums[i - 1]
    nums2[i] = nums2[i] + nums2[i - 1]

q = int(input())
for _ in range(q):
    t, l, r = map(int, input().split())

    if t == 1:
        Sum = nums[r - 1] - (nums[l - 2] if l > 1 else 0)
        print(Sum)
    else:
        Sum = nums2[r - 1] - (nums2[l - 2] if l > 1 else 0)
        print(Sum)