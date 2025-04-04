# Problem: Masha and a Beautiful Tree - https://codeforces.com/problemset/problem/1741/D

t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    count = 0

    def mergeSort(left, right):
        global count
        if left == right:
            return [nums[left]]
        
        mid = left + (right - left) // 2

        left_sorted = mergeSort(left, mid)
        right_sorted = mergeSort(mid + 1, right)

        # do the ckecks here
        if left_sorted[0] < right_sorted[0]:
            return left_sorted + right_sorted
        else:
            count += 1
            return right_sorted + left_sorted
    
    if mergeSort(0, len(nums) - 1) == sorted(nums):
        print(count)
    else:
        print(-1)