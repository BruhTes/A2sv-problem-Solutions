# Problem: Presents - https://codeforces.com/problemset/problem/136/A

def presents(friends):
    result = [None] * len(friends)

    for pi, i in enumerate(friends):
        result[i - 1] = pi + 1

    return " ".join(map(str, result))

def main():
    t = int(input().strip())
    friends = list(map(int, input().split()))
    print(presents(friends))

if __name__ == "__main__":
    main()
