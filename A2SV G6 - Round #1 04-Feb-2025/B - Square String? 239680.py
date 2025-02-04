# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

t = int(input())

for _ in range(t):
    string = input()
    if len(string) % 2 != 0:
        print("NO")
    else:
        if len(string) == 2:
            if string[0] == string[1]:
                print("YES")
            else:
                print("NO")

        elif (string[0:len(string) // 2] == string[len(string) // 2 : len(string)]):
            print("YES")
        else:
            print("NO")



