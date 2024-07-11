class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)
        s = binary_str[::-1]
        return int(s,2)