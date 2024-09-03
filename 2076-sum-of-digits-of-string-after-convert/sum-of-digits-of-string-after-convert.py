class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alphabet = {chr(i + ord('a')): i + 1 for i in range(26)}
        num_str = ''.join(str(alphabet[char]) for char in s)

        result = sum(int(digit) for digit in num_str)
        for _ in range(1, k):
            result = sum(int(digit) for digit in str(result))
        
        return result

