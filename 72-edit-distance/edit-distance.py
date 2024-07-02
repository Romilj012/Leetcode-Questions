class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dpCache = [[float("inf")] * (len(word2) + 1) for i in range(len(word1)+1)]
        for i in range(len(word1) + 1):
            dpCache[i][len(word2)] = len(word1) - i
        for j in range(len(word2)+1):
            dpCache[len(word1)][j] = len(word2) - j

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i] == word2[j]:
                    dpCache[i][j] = dpCache[i+1][j+1]
                else:
                    dpCache[i][j] = 1 + min(dpCache[i+1][j], dpCache[i][j+1], dpCache[i+1][j+1])
        return dpCache[0][0]
            

