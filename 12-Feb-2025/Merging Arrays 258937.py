# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

def merge(a, b, nums1, nums2):
    merged = []
    p1 = 0
    p2 = 0

    while p1 < a and p2 < b:
        if nums1[p1] <= nums2[p2]:
            merged.append(nums1[p1])
            p1 += 1
        else:
            merged.append(nums2[p2])
            p2 += 1
    merged.extend(nums1[p1:])
    merged.extend(nums2[p2:])
    
    return merged

a, b = map(int, input().split())

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(*merge(a, b, nums1, nums2))