# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
        title = []
        
        while columnNumber > 0:
            columnNumber -= 1
            remainder = columnNumber % 26
            title.append(letters[remainder])
            columnNumber //= 26
        
        return ''.join(title[::-1])
