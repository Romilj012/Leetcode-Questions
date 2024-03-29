class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lis = []
        for i in range(left, right + 1):
            if self.isSelfDividing(i):
                lis.append(i)
        return lis
    
    def isSelfDividing(self, num: int) -> bool:
        temp = num
        while temp > 0:
            digit = temp % 10
            if digit == 0 or num % digit != 0:
                return False
            temp //= 10
        return True
