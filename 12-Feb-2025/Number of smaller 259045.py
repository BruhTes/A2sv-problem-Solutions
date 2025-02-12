# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

def num_of_smaller(a, b, nums1, nums2):
    result = []
    j = 0
    count = 0

    for i in range(b):
        while j < a and nums2[i] > nums1[j]:
            count += 1
            j += 1
        result.append(count)

    return result   


a, b = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(*num_of_smaller(a, b, nums1, nums2))