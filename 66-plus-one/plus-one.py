class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        num = 0
        for i in digits:
            s+=str(i)
        num = int(s) + 1
        return list(map(int, str(num)))


