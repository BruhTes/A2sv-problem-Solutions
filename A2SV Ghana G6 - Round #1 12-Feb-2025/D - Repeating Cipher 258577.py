# Problem: D - Repeating Cipher - https://codeforces.com/gym/585132/problem/D

t = int(input())
encrypted = input()

decrypted = ""

i = 0
j = 0
while i < t:
    decrypted += encrypted[i]
    j += 1
    i = i + j
    
print(decrypted)