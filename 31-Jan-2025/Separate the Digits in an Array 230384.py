# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for num in nums:
            # if num % 10 == 0:
            #     answer.append(num)
            # else:
                temp = []

                while (num > 0):
                    temp.append(num%10)
                    num //= 10
                answer = answer + temp[::-1]

        return answer