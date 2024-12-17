class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        result = 0
        while i < n and s[i] == ' ':
            i += 1
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31-1 if sign == 1 else -2**31
            result = result * 10 + digit
            i += 1
        return sign * result
        