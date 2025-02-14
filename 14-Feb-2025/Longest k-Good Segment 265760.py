# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

def longest_good_segment(n, k, nums):
    uniques = set()
    left = 0
    result = [1, 1]

    for right in range(n):
        uniques.add(nums[right])

        while len(uniques) > k:
            uniques.remove(nums[left])
            left += 1

        if right - left > result[1] - result[0]:
            result = [left + 1, right + 1]
    
    return result

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(*longest_good_segment(n, k, nums))
