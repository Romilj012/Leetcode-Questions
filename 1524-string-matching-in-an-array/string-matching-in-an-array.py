class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        arr = " ".join(words)
        res = [word for word in words if arr.count(word) >= 2]
        return res

        