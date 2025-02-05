# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        romans = {1 : "I", 5 : "V", 10 : "X", 50 : "L", 100 : "C", 500 : "D", 1000 : "M", 4 : "IV", 9 : "IX", 40 : "XL", 90 : "XC", 400 : "CD", 900 : "CM"}

        roman = []
        i = 1000

        while num > 0 and i > 0:
            temp = num // i
            
            if temp == 4 or temp == 9:
                roman.append(romans[temp * i])
            elif temp != 0:
                if temp >= 5 and temp <=8 and i != 1000:
                    roman.append(romans[5 * i])
                    roman.append(romans[i] * (temp % 5))
                elif temp * i in romans:
                    roman.append(romans[temp * i])
                else:
                    roman.append(romans[i] * temp)
            
            num %= i
            i //= 10

        return "".join(roman)