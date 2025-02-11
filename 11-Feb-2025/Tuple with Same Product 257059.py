# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums_length = len(nums)
        nums.sort()

        products = {}

        for i in range(nums_length):
            for j in range(i + 1, nums_length):
                product = nums[i] * nums[j]
                if product in products: 
                    products[product] += 1
                else:
                    products[product] = 1
        

        total_same = 0
        for product, count in products.items():
            if count > 1:
                total_same += count*(count-1)//2

        return total_same * 8
