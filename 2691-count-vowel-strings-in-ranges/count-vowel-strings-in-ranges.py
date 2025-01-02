class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = ['a', 'e', 'i', 'o', 'u']
        prefixCnt = [0] * (len(words) + 1)
        prev = 0
        for i, word in enumerate(words):
            if word[0] in vowel and word[-1] in vowel:
                prev += 1
            prefixCnt[i+1] = prev
        result = [0] * len(queries)
        for i, q in enumerate(queries):
            l, r = q
            result[i] = prefixCnt[r+1] - prefixCnt[l]
        return result
        