# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

n, k = map(int, input().split())
nums = list(map(int, input().split()))

max_queue = deque()
min_queue = deque()
count = 0
left = 0

for right in range(len(nums)):
    while max_queue and max_queue[-1] < nums[right]:
        max_queue.pop()
    max_queue.append(nums[right])

    while min_queue and min_queue[-1] > nums[right]:
        min_queue.pop()
    min_queue.append(nums[right])

    while max_queue and min_queue and max_queue[0] - min_queue[0] > k:
        if max_queue[0] == nums[left]:
            max_queue.popleft()
        if min_queue[0] == nums[left]:
            min_queue.popleft()
        left += 1
    
    # count the number of subarrays in the sunarray you have found
    count += (right - left + 1)

'''
    # x = right - left + 1
    # if x == 1 and nums[right] <= k:
    #     count += 1
    # else:
    #     count += (x * (x + 1)) // 2
    
    # print('right : ', right, ' : ', count)'
'''

print(count)