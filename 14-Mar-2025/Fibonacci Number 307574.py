# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def fibonacci(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in memo:
                return memo[n]
            
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return memo[n]
        
        return fibonacci(n)
