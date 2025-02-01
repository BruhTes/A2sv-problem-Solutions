# Problem: sWapCaSe - https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    result = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                result += char.lower()
            else:
                result += char.upper()
        else:
            result += char
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)