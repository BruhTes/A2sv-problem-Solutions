# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def calculate_diagonal_sum(board, row, col, n, m):
    directions = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    total = 0
    
    for dx, dy in directions:
        curr_row, curr_col = row, col
        while 0 <= curr_row < n and 0 <= curr_col < m:
            total += board[curr_row][curr_col]
            curr_row += dx
            curr_col += dy
            
    return total - 3 * board[row][col]

def find_max_attack_position(board, n, m):
    return max(
        calculate_diagonal_sum(board, i, j, n, m)
        for i in range(n)
        for j in range(m)
    )

def solve_test_case():
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    return find_max_attack_position(board, n, m)

def main():
    t = int(input())
    for _ in range(t):
        print(solve_test_case())

if __name__ == "__main__":
    main()