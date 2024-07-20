class Solution:
    def isHappy(self, n: int) -> bool:
        def square(n):
            return sum(int(digit)**2 for digit in str(n))
        s = set()
        while n!= 1 and n not in s:
            s.add(n)
            n = square(n)
        return n == 1