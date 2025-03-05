# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = defaultdict(int)
        stack = []
        for i in range(len(nums2) - 1, -1, -1):
            if not stack:
                stack.append(nums2[i])
                nextGreater[nums2[i]] = -1
            else:
                while stack and stack[-1] < nums2[i]:
                    stack.pop()
                if stack:
                    nextGreater[nums2[i]] = stack[-1]
                else:
                    nextGreater[nums2[i]] = -1
                stack.append(nums2[i])

        for i in range(len(nums1)):
            nums1[i] = nextGreater[nums1[i]]
        
        return nums1
                