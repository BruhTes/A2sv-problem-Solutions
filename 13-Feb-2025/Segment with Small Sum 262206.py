# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

def findSegment(n, s, nums):
    left = 0
    right = 0
    window_sum = 0
    max_len = 0

    while right < n:
        window_sum += nums[right]

        while window_sum > s:
            window_sum -= nums[left]
            left += 1

        max_len = max(max_len, right - left + 1)
        right += 1
    
    return max_len


n, s = map(int, input().split())
nums = list(map(int, input().split()))
print(findSegment(n, s, nums))