# Problem: Sum of Subarray Minimums - https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        next_smallest = [len(arr) for i in range(len(arr))]
        prev_smallest = [-1 for i in range(len(arr))]
        n = len(arr)
        mod = 10**9 + 7
        
        # the next smallest elements
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            
            if stack:
                next_smallest[i] = stack[-1]
            
            stack.append(i)

        # prev smallest elements
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            
            if stack:
                prev_smallest[i] = stack[-1]
            
            stack.append(i)
        
        print(next_smallest)
        print(prev_smallest)

        # calculate the sum
        result = 0
        for i in range(n):
            count = (i - prev_smallest[i]) * (next_smallest[i] - i)
            result += (arr[i]) * count
            print("i : ", result)
        return result % mod