# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.split("@")
            name = name.lower()
            domain = domain.lower()
            name = name[0] + "*****" + name[len(name) - 1]
            return name + "@" + domain
        else:
            digits = ""

            for d in s:
                if d.isdigit():
                    digits += d

            n = len(digits)
            if n > 10:
                return "+" + "*"*(n - 10) + "-***-***-" + digits[-4:]
            return "***-***-" + digits[-4:]