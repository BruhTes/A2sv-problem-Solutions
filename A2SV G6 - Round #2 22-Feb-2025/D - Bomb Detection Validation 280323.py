# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

# Directions for 8 possible neighbors (top-left, top, top-right, left, right, bottom-left, bottom, bottom-right)
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_valid_field(n, m, field):
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                continue
            
            if '1' <= field[i][j] <= '8':
                expected_bombs = int(field[i][j])
                actual_bombs = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                        actual_bombs += 1
                if actual_bombs != expected_bombs:
                    return "NO"
            
            if field[i][j] == '.':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and field[ni][nj] == '*':
                        return "NO"
    
    return "YES"


n, m = map(int, input().split()) 
field = [input().strip() for _ in range(n)]

print(is_valid_field(n, m, field))
