# Problem: Convert the Temperature - https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        converted = []

        converted.append(celsius + 273.15)
        converted.append(celsius*1.80 + 32)

        return converted