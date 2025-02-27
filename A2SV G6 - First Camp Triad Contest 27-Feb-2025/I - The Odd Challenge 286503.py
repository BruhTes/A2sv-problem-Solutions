# Problem: I - The Odd Challenge - https://codeforces.com/gym/589822/problem/I

t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))
    
    for i in range(1, n):
        nums[i] = nums[i - 1] + nums[i]

    for _ in range(q):
        l, r, k = map(int, input().split())
        
        current_sum = nums[-1] - nums[r - 1] - (nums[l - 2] if l - 2 >= 0 else 0) + ((r - l + 1) * k)

        if current_sum % 2 == 0:
            print("NO")
        else:
            print("YES")