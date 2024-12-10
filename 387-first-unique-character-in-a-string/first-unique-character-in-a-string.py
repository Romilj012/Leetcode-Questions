class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = defaultdict(int)
        for char in s:
            char_count[char] += 1
        for k, v in char_count.items():
            if v == 1:
                return s.index(k)
        return -1
        