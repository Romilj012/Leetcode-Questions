class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for num in range(1,n+1):
            ones = lambda num: bin(num).count('1')
            ans.append(ones(num))
        return ans