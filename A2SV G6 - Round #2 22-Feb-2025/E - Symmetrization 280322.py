# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

for _ in range(int(input())):
    n = int(input())
    mat = [list(map(int, input().strip())) for _ in range(n)]
    
    mat9 = [list(x) for x in zip(*mat[::-1])]
    mat18 = [list(x) for x in zip(*mat9[::-1])]
    mat27 = [list(x) for x in zip(*mat18[::-1])]

    count = 0

    for i in range(n):
        for j in range(n):
            total = mat[i][j] + mat9[i][j] + mat18[i][j] + mat27[i][j]
            
            if total == 1 or total == 3:
                count += 1
            elif total == 2:
                count += 2

    print(count // 4)
