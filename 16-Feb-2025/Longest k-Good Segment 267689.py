# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

def solve():
    [num_books, max_distinct] = list(map(int, input().split()))
    books = list(map(int, input().split()))
    
    element_count = {}
    start, end, left = 0, 0, 0

    for right in range(num_books):

        if books[right] not in element_count:
            element_count[books[right]] = 0

        element_count[books[right]] += 1
        
        while len(element_count) > max_distinct:
            element_count[books[left]] -= 1

            if element_count[books[left]] == 0:
                del element_count[books[left]]
            left += 1

      
        if len(element_count) <= max_distinct and right - left + 1 > end - start + 1:
            start, end = left, right

    print(start + 1, end + 1)


if __name__ == "__main__":
    num_cases = 1
    for _ in range(num_cases):
        solve()
