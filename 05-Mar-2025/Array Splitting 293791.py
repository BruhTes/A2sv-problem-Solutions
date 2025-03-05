# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

def arraySplit():
   n, k = map(int, input().split())
   a = list(map(int, input().split()))

# splitting between two numbers saves you their difference
   diff = [a[i-1] - a[i] for i in range(1, n)]    
   diff.sort()
   res = a[-1] - a[0]

# subtract (k - 1) the max diff saved
   for i in range(k - 1):
      res += diff[i]
    
   return res

print(arraySplit())