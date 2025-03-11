# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

t = int(input())

for _ in range(t):
    n = int(input())
    nums = input()

    temp = 1
    stackZero = []
    stackOne = []
    result = []

    for char in nums:
        if char == '0':
            if stackOne:
                result.append(stackOne[-1])
                stackZero.append(stackOne.pop())
            else:
                stackZero.append(temp)
                result.append(temp)
                temp += 1
        else:
            if stackZero:
                result.append(stackZero[-1])
                stackOne.append(stackZero.pop())
            else:
                stackOne.append(temp)
                result.append(temp)
                temp += 1
    print(len(stackZero) + len(stackOne))
    print(*result)        