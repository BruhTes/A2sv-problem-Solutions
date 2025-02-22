# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

k = int(input())
binary = input()

oneMap = {0 : 1}
onesCount = 0
count = 0

for char in binary:
    if char == "1":
        onesCount += 1
    
    if onesCount - k in oneMap:
        count += oneMap[onesCount - k]
    
    oneMap[onesCount] = oneMap.get(onesCount, 0) + 1

print(count)